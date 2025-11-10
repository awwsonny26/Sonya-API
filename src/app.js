import express from 'express';
import dotenv from 'dotenv';
import { usersRouter } from './routes/users.js';
import { categoriesRouter } from './routes/categories.js';
import { recordsRouter } from './routes/records.js';
import { errorHandler } from './middlewares/errorHandler.js';

dotenv.config();

const app = express();

app.use(express.json());

app.get('/health', (req, res) => {
  res.json({ 
    status: 'ok',
    date: new Date().toISOString(),
  });
});

app.use('/user', usersRouter);
app.use('/category', categoriesRouter);
app.use('/record', recordsRouter);

app.use(errorHandler);

export default app;
