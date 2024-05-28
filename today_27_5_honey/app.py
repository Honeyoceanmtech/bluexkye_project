

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy.dialects import postgresql


Base = declarative_base()
metadata = Base.metadata




class User(Base):
    __tablename__ = "user"
    id = Column("id",Integer,primary_key=True)
    user_name = Column("user_name",String)
    email = Column("email",String)
    created_at = Column('created_at',postgresql.TIMESTAMP())
    

    def __init__(self,id,user_name,email,created_at):
        self.id = id
        self.user_name = user_name
        self.email = email
        self.created_at = created_at
    
    def __repr__(self):
        return f"({self.id} {self.user_name}  {self.email} {self.created_at})"
 
 
class Post(Base):
    __tablename__ = "post"
    id = Column("id",Integer,primary_key=True)
    title = Column("Post_title",String)
    content = Column("Post_content",String)
    user_id = Column(Integer ,  ForeignKey("user.id"))
    created_at = Column('created_at',postgresql.TIMESTAMP())
    

    def __init__(self,id,title,content,user_id,created_at):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.created_at = created_at
        
        
    def __repr__(self):
        return f"({self.id} {self.title}  {self.content} {self.user_id} {self.created_at})"
    
   
class Comment(Base):
    __tablename__ = "comment"
    
    id = Column("id",Integer,primary_key=True)
    post_id = Column(Integer , ForeignKey("post.id"))
    user_id = Column(Integer ,  ForeignKey("user.id"))
    created_at = Column('created_at',postgresql.TIMESTAMP())
    comment_content = Column("comment_content",String)
    comment_views = Column("comment_views",Float)
    

    def __init__(self,id,post_id,user_id,created_at,comment_content,comment_views):
        self.id = id
        self.post_id = post_id
        self.user_id = user_id
        self.created_at = created_at
        self.comment_content = comment_content
        self.comment_views = comment_views
        
    def __repr__(self):
        return f"({self.id} {self.post_id}  {self.user_id} {self.created_at} {self.comment_content} {self.comment_views})"
    
 
 
    
class Category(Base):
    __tablename__ = "category"
    
    id = Column("id",Integer,primary_key=True)
    Category_name = Column(String)
    created_at = Column('created_at',postgresql.TIMESTAMP())
    
        
    def __init__(self,id,Category_name,created_at):
        self.id = id
        self.Category_name = Category_name
        self.created_at = created_at
        
    def __repr__(self):
        return f"({self.id} {self.Category_name} {self.created_at})"
    
 
class Post_category(Base):
    __tablename__ = "post_category"
    id = Column("id",Integer,primary_key=True)
    post_id = Column("post_id",ForeignKey("post.id"),primary_key=True)
    category_id = Column("category_id",ForeignKey("category.id"),primary_key=True)
    created_at = Column('created_at',postgresql.TIMESTAMP())
    
    
    def __init__(self,id,post_id,category_id,created_at):
        self.id = id
        self.post_id = post_id
        self.category_id = category_id
        self.created_at = created_at
        
    def __repr__(self):
        return f"({self.id} {self.post_id}  {self.category_id} {self.created_at})"
    




engine = create_engine('{Add database url}',echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# # # plan details
user1 = User(1,'user1','user1@gmail.com',datetime.datetime.now())
user2 = User(2,"user2","user2@gmail.com",datetime.datetime.now())
# # # session.add(user1)
# # # session.add(user2)


# # post details
postuser1 = Post(1,"instagram Post","instagram is very useable social-media",user1.id,datetime.datetime.now())
postuser2 = Post(2,"Twitter Post","Twitter is very useful social-media platform",user2.id,datetime.datetime.now())
# session.add(postuser1)
# session.add(postuser2)


# # Comment details
Comment1 = Comment(1,postuser1.id,user1.id,datetime.datetime.now(),"Happy Mood",1.7)
Comment2 = Comment(2,postuser2.id,user2.id,datetime.datetime.now(),"Have a Nice Day",2.5)
# session.add(Comment1)
# session.add(Comment2)




# # Category details
category1 = Category(1,"Funny posts",datetime.datetime.now())
category2 = Category(2,"Friendship posts",datetime.datetime.now())
# session.add(category1)
# session.add(category2)




# # Profile details
post_category1 = Post_category(1,postuser1.id,category1.id,datetime.datetime.now())
post_category2 = Post_category(2,postuser2.id,category2.id,datetime.datetime.now())
# session.add(post_category1)
# session.add(post_category2)



# result = session.query(Comment)
# for x in result:
#     print(x)
    
session.commit()


