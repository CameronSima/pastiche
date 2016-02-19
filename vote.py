import utilities
import settings

class Vote(object):
    def __init__(self, id, vote):
        self.id = id
        self.vote = self.get_vote_value(vote)
        self.conn, self.c = utilities.connect_to_db(settings.DB)

    def increment_vote(self):
        self.c.execute("UPDATE poems SET likes = likes + ? WHERE id=?", 
                                                  (self.vote, int(self.id)))
        self.conn.commit()
    
    def return_likes(self):
        self.c.execute("SELECT likes FROM poems WHERE id=?", self.id)
        return self.c.fetchone()

    def close_conn(self):
        self.conn.close()

    def get_vote_value(self, vote):
        if vote == 'up':
            return 1
        elif vote == 'down':
            return -1
        elif vote == 'upup':
            return 2
        elif vote == 'downdown':
            return -2
        else:
            return 0
        


