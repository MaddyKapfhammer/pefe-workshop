using System;
using System.Collections.Generic;

public class UserService
{
    private readonly IDatabase db;

    public UserService(IDatabase database)
    {
        db = database;
    }

    public Dictionary<string, string> CreateUser(string name, string email)
    {
        Console.WriteLine($"Creating user: {name}");
        var user = new Dictionary<string, string> {
            { "name", name },
            { "email", email }
        };
        db.Save(user);
        return user;
    }

    public bool DeleteUser(string userId)
    {
        var user = db.Get(userId);
        if (user != null)
        {
            Console.WriteLine($"Deleting user ID: {userId}");
            db.Delete(userId);
            return true;
        }
        return false;
    }
}

public interface IDatabase
{
    void Save(Dictionary<string, string> user);
    Dictionary<string, string> Get(string userId);
    void Delete(string userId);
}
