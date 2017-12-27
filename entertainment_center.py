import media
import fresh_tomatoes

rock_dog = media.Movie("Rock Dog",
                        "Bodi discovers a radio that fell from the sky",
                        "https://m.aceshowbiz.com/webimages/still/preview/rock-dog-poster07.jpg",
                        "https://www.youtube.com/watch?v=O5EPq94P7G4")
 
ragnarok = media.Movie("Ragnarok",
                   "Imprisoned on the otherside of the universe,The might Thor finds himself in a deadly gladiator contest with The Hulk",
                   "https://cdn.flickeringmyth.com/wp-content/uploads/2017/11/Thor-Ragnarok-banner-3-1-600x372-600x372.jpg",
                   "https://www.youtube.com/watch?v=ue80QwXMRHg")

avengers_infinity_war = media.Movie("Avengers Infinity War",
                        "Thanos arrives on earth to collect the infinity stones",
                        "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/7/7e/Avengers_Infinity_War_SDCC_poster.jpg/revision/latest?cb=20170724003836",
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

black_panther = media.Movie("Black Panther",
                   "King T'challa returns home to wakanda,but two enemies conspire to bring him down.",
                   "https://pre00.deviantart.net/512d/th/pre/f/2017/059/2/e/black_panther___mock_movie_poster_by_bryanunderwood-db0qo1y.jpg",
                   "https://www.youtube.com/watch?v=xjDjIWPwcPU")

spiderman_homecoming = media.Movie("Spiderman - Homecoming",
                   "Thrilled by his experience with the Avengers,young peter parker returns home to live with his Aunt May",
                   "http://s1.1zoom.me/big0/487/Spider-Man_Homecoming_Spiderman_hero_Heroes_comics_532677_1280x623.jpg",
                   "https://www.youtube.com/watch?v=U0D3AOldjMU")

justice_league = media.Movie("Justice League",
                   "Batman and Wonder woman work quickly to recruit a team to stand against newly awakened enemy.",
                   "http://cdn.collider.com/wp-content/uploads/2017/10/justice-league-poster-social.jpg",
                   "https://www.youtube.com/watch?v=r9-DM9uBtVI")                   
                   
                        
#print(avengers2.title)
#avengers2.show_trailer()

movies =[rock_dog ,avengers_infinity_war, ragnarok, black_panther,spiderman_homecoming,justice_league]
fresh_tomatoes.open_movies_page(movies)
