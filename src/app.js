import express from 'express';
import dotenv from 'dotenv';
import { authRequired } from './middlewares/auth.js'
import { errorHandler } from './middlewares/errorHandler.js';
import authRouter from './routes/auth.js'
import usersRouter from './routes/users.js';
import categoriesRouter from './routes/categories.js';
import recordsRouter from './routes/records.js';

dotenv.config();

const app = express();

app.use(express.json());

app.get('/health', (req, res) => {
  res.json({ 
    status: 'ok',
    date: new Date().toISOString(),
  });
});

app.use('/auth', authRouter);

app.use('/user', authRequired, usersRouter);
app.use('/category', authRequired, categoriesRouter);
app.use('/record', authRequired, recordsRouter);

app.use(errorHandler);

export default app;
