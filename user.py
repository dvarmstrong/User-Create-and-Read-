from mysqlconnection import connectToMySQL
# Model the User_schema Database
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# method to query the database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # call the connectToMySQL function with the schema you are targeting
        results = connectToMySQL('user_schema').query_db(query)
        # Create an empty list to append our instances of users
        users = []
# Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ( %(First Name)s, %(Last Name)s, %(Email)s, NOW(), NOW() );" 
        result = connectToMySQL('user_schema').query_db(query,data)
        return result


    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('user_schema').query_db(query,data)




        