class Article:

    all=[]
    
    def __init__(self,author,magazine,title):
        self.author=author
        self.magazine=magazine
        self.title=title
        #author.articles.append(self)
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        from lib.Author import Author
        if(not type(author)==Author):
            raise ValueError("author must be an instance of Author")
        self._author=author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        from lib.Magazine import Magazine
        if(not type(magazine)==Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        self._magazine=magazine

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if(not type(title)==str):
            raise ValueError("Title must be a string")
        self._title=title


