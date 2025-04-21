function processUserData(data) {
  return data.filter(d => d.active).map(d => ({
    name: d.name,
    email: d.email,
    lastLogin: d.lastLogin,
    score: calculateScore(d),
    status: determineStatus(d.lastLogin)
  }));
}

function calculateScore(user) {
  const clicks = user.clicks || 0;
  const shares = user.shares || 0;
  return Math.round(((clicks * 2 + shares * 3) / 5) * 100) / 100;
}

function determineStatus(lastLogin) {
  if (!lastLogin) return 'unknown';
  const last = new Date(lastLogin);
  const now = new Date();
  const daysInactive = Math.floor((now - last) / (1000 * 60 * 60 * 24));
  return daysInactive > 30 ? 'inactive' : 'active';
}
