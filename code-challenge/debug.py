#!/usr/bin/env python3
import ipdb;

from faker import Faker

from lib.Author import Author
from lib.Magazine import Magazine
from lib.Article import Article


if __name__ == '__main__':
    print("Testing....")
    faker=Faker()
    print("Authors:")
    for i in range(5):
        Author(faker.name())
    for author in Author.all:
        print(author.name)
    print()
    print("Magazines:")
    magazine_names=["Cosmo Girl","Cosmopolitan","Sports Illistrated","People's Magazine","Forbes","The New Yorker","The New York Times"]
    magazine_categories=["beauty","beauty","sports","gossip","politics","news","news"]
    for i in range(len(magazine_names)):
        Magazine(magazine_names[i],magazine_categories[i])
    for magazine in Magazine.all:
        print(magazine.name)
    article_titles=["dating tips","make up tips","football data","Oprah's new show","Biden's election results","AWS conference in Javits","Subway crime down"]
    print()
    print("Articles:")
    for i in range(5):
        Author.all[i].add_article(Magazine.all[i],article_titles[i])
    Author.all[0].add_article(Magazine.all[0],"dating tips part 2")
    for article in Article.all:
        print(article.author.name)

    ipdb.set_trace()
