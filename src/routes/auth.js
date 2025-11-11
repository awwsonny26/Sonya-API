import express from 'express';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { prisma } from '../prisma.js';
import { registerSchema, loginSchema } from '../validation.js'

const authRouter = express.Router();

authRouter.post('/register', async (req, res, next) => {
  try {
    const { error, value } = registerSchema.validate(req.body);
    if (error) return res.status(400).json({ message: error.message });

    const existing = await prisma.user.findUnique({
      where: { username: value.username },
    });
    if (existing) {
      return res
        .status(400)
        .json({ message: 'User with this username already exists' });
    }

    const hash = await bcrypt.hash(value.password, 10);

    const user = await prisma.user.create({
      data: {
        username: value.username,
        password: hash,
      },
      select: { id: true, username: true },
    });

    res.status(201).json(user);
  } catch (err) {
    next(err);
  }
});

authRouter.post('/login', async (req, res, next) => {
  try {
    const { error, value } = loginSchema.validate(req.body);
    if (error) return res.status(400).json({ message: error.message });

    const user = await prisma.user.findUnique({
      where: { username: value.username },
    });

    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    const ok = await bcrypt.compare(value.password, user.password);
    if (!ok) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    const token = jwt.sign(
      { sub: user.id },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN || '1h' }
    );

    res.json({
      access_token: token,
      token_type: 'Bearer',
      expires_in: process.env.JWT_EXPIRES_IN || '1h',
    });
  } catch (err) {
    next(err);
  }
});

export default authRouter;
