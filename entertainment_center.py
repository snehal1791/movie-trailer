import fresh_tomatoes
import media

""" Creating and assiging values to different movies """

finding_nemo = media.Movie("Finding Nemo",
                            "May 30, 2003 (USA)",
                            "Andrew Stanton, Lee Unkrich",
                            "http://ia.media-imdb.com/images/M/MV5BOTdhMTQzNTMtNTkwZC00ZTAwLTgwMmEtNGJhOGViYWNhMTc4XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UY268_CR3,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=wZdpNglLbt8")

finding_dory = media.Movie("Finding Dory",
                            "June 17, 2016 (USA)",
                            "Andrew Stanton, Angus MacLane",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg",
                            "https://www.youtube.com/watch?v=3JNLwlcPBPI")

tangled = media.Movie("Tangled",
                        "November 24, 2010 (Canada)",
                        "Nathan Greno, Byron Howard",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Tangled_poster.jpg/220px-Tangled_poster.jpg",
                        "https://www.youtube.com/watch?v=ip_0CFKTO9E")

kung_fu_panda = media.Movie("Kung Fu Panda",
                            "June 6, 2008 (USA)",
                            "Mark Osborne, John Stevenson",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

kung_fu_panda_2 = media.Movie("Kung Fu Panda 2",
                                "May 26, 2011 (USA)",
                                "Jennifer Yuh Nelson",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/b/b1/Kung_Fu_Panda_2_Poster.jpg/220px-Kung_Fu_Panda_2_Poster.jpg",
                                "https://www.youtube.com/watch?v=YIW5oo-8NYw")

kung_fu_panda_3 = media.Movie("Kung Fu Panda 3",
                                "January 29, 2016 (USA)",
                                "Jennifer Yuh Nelson, Alessandro Carloni",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Kung_Fu_Panda_3_poster.jpg/220px-Kung_Fu_Panda_3_poster.jpg",
                                "https://www.youtube.com/watch?v=10r9ozshGVE")

""" Array to store movies """
movies = [finding_nemo, finding_dory, tangled, kung_fu_panda, kung_fu_panda_2, kung_fu_panda_3]
""" Generates movie trailer webpage """
fresh_tomatoes.open_movies_page(movies)
