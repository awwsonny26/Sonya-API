import Joi from 'joi';

export const userSchema = Joi.object({
  username: Joi.string().min(3).required(),
  password: Joi.string().min(6).required(),
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

export const registerSchema = Joi.object({
  username: Joi.string().min(3).max(64).required(),
  password: Joi.string().min(6).max(128).required(),
});

export const loginSchema = Joi.object({
  username: Joi.string().required(),
  password: Joi.string().required(),
});
