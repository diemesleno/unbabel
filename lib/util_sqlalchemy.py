from project.extensions import db


class ResourceMixin(object):
    """ 
    Mixin class to handle some commom database functions
    """
    def save(self):
        """ 
        Save a model instance.

        :return: Model instance
        """
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        """ 
        Update a model instance.

        :return: db.session.commit()'s result
        """
        return db.session.commit()
    
    def __str__(self):
        """ 
        Create a human readable version of a class instance.

        :return: self
        """
        obj_id = hex(id(self))
        columns = self.__table__.c.keys()
        
        values = ', '.join("%s=%r" % (n, getattr(self, n)) for n in columns)
        return '<%s %s(%s)>' % (obj_id, self.__class__.__name__, values)
