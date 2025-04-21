class UserService {
  constructor(database) {
    this.db = database;
  }

  createUser(name, email) {
    const user = { name, email };
    console.log("Creating user:", name);
    this.saveToDb(user);
    return user;
  }

  deleteUser(userId) {
    const user = this.getUser(userId);
    if (user) {
      console.log("Deleting user ID:", userId);
      this.removeFromDb(userId);
      return true;
    }
    return false;
  }

  saveToDb(user) {
    this.db.save(user);
  }

  getUser(userId) {
    return this.db.get(userId);
  }

  removeFromDb(userId) {
    this.db.delete(userId);
  }
}
