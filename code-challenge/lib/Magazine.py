class Magazine:

    all=[]
    
    def __init__(self,name,category):
        self.name=name
        self.category=category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if(not type(name)==str):
            raise ValueError("Name must be a string")
        self._name=name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,category):
        if(not type(category)==str):
            raise ValueError("Category must be a string")
        self._category=category

    def contributors(self):
        from lib.Article import Article
        return [article.author for article in Article.all if article.magazine==self]

    def article_titles(self):
        from lib.Article import Article
        return [article.title for article in Article.all if article.magazine==self]
    
    def contributing_authors(self):
        return list(set([author for author in self.contributors() if len(author.articles())>2]))
        # contributers=self.contributors()
        # entry_records={}
        # for contributor in contributers:
        #     if contributor not in entry_records:
        #         entry_records[contributor]=1
        #     else:
        #        entry_records[contributor]+=1
        
        # c_a=[]
        # for author in entry_records.keys():
        #     if(entry_records[author]>2):
        #         c_a.append(author)
        # return c_a