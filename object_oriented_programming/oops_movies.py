class Movie:

    title:str

    rating:int

    runtime:int

    director:str

    genre:str

    def set_movie(self,title,rating,runtime,director,genre):  #=> initialize instance variables

        self.title=title

        self.rating=rating

        self.runtime=runtime

        self.director=director

        self.genre=genre

    def display(self):

        print(self.title,self.rating,self.runtime,self.director,self.genre)

movie_instance1=Movie()

movie_instance2=Movie()

movie_instance1.set_movie("ARM",4,160,"Jithin Lal","Action Adventure")

movie_instance1.display()

   

  