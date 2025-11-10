import Joi from 'joi';

export const userSchema = Joi.object({
  name: Joi.string().min(2).required(),
});

export const categorySchema = Joi.object({
  title: Joi.string().min(2).required(),
  isGlobal: Joi.boolean().default(false),
  ownerId: Joi.number().optional().allow(null),
});

export const recordSchema = Joi.object({
  userId: Joi.number().required(),
  categoryId: Joi.number().required(),
  amount: Joi.number().positive().required(),
  createdAt: Joi.date().optional(),
});
