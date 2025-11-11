import express from 'express';
import { prisma } from '../prisma.js';
import { categorySchema } from '../validation.js';

const categoriesRouter = express.Router();

categoriesRouter.post('/', async (req, res, next) => {
  try {
    const { error, value } = categorySchema.validate(req.body);
    if (error) return res.status(400).json({ error: error.message });

    const category = await prisma.category.create({ data: value });
    res.status(201).json(category);
  } catch (err) {
    next(err);
  }
});

categoriesRouter.get('/', async (req, res, next) => {
  try {
    const categories = await prisma.category.findMany();
    res.json(categories);
  } catch (err) {
    next(err);
  }
});

categoriesRouter.delete('/:id', async (req, res, next) => {
  try {
    await prisma.category.delete({
      where: { id: parseInt(req.params.id) },
    });
    res.status(204).end();
  } catch (err) {
    next(err);
  }
});

export default categoriesRouter;
