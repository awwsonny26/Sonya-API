import jwt from 'jsonwebtoken';

export function authRequired(req, res, next) {
  try {
    const header = req.headers.authorization || '';
    const [scheme, token] = header.split(' ');

    if (scheme !== 'Bearer' || !token) {
      return res.status(401).json({
        message: 'Authorization token missing',
        error: 'authorization_required',
      });
    }

    const payload = jwt.verify(token, process.env.JWT_SECRET);
    req.user = { id: payload.sub };
    next();
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      return res.status(401).json({
        message: 'The token has expired.',
        error: 'token_expired',
      });
    }
    return res.status(401).json({
      message: 'Invalid token.',
      error: 'invalid_token',
    });
  }
}
