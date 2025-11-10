import express from 'express';
import { prisma } from '../prisma.js';
import { recordSchema } from '../validation.js';

export const recordsRouter = express.Router();

recordsRouter.post('/', async (req, res, next) => {
  try {
    const { error, value } = recordSchema.validate(req.body);
    if (error) return res.status(400).json({ error: error.message });

    const record = await prisma.record.create({ data: value });
    res.status(201).json(record);
  } catch (err) {
    next(err);
  }
});

recordsRouter.get('/', async (req, res, next) => {
  try {
    const records = await prisma.record.findMany({
      include: { user: true, category: true },
    });
    res.json(records);
  } catch (err) {
    next(err);
  }
});

recordsRouter.delete('/:id', async (req, res, next) => {
  try {
    await prisma.record.delete({
      where: { id: parseInt(req.params.id) },
    });
    res.status(204).end();
  } catch (err) {
    next(err);
  }
});
