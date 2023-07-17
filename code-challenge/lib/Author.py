class Author:
    
    all=[]

    def __init__(self,name):
        self.name=name
        #self.articles=[]
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if(hasattr(self,"name")):
            raise ValueError("Name cannot be changed")
        if(not type(name)==str):
            raise ValueError("Name must be a string")
        self._name=name

    def articles(self):
        from lib.Article import Article
        return [article for article in Article.all if article.author==self]
        # articles=[]
        # for article in Article.all:
        #     if(article.author==self):
        #         articles.append(article)
        # return articles
    
         #return self.articles

    def magazine(self):
        from lib.Article import Article
        return list(set([article.magazine for article in Article.all if article.author==self]))
    
    def add_article(self,magazine,title):
        from lib.Article import Article
        Article(self,magazine,title)

    def topic_areas(self):
        from lib.Article import Article
        return list(set([article.magazine.category for article in self.articles()]))


    
