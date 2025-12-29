"""Famous artists database - ~1095 artists with rotation support."""

from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Artist:
    """Artist information."""
    name: str
    birth_year: int
    style: str
    description: str


# Multiple artists per date for variety - rotation based on hour
ARTISTS_BY_DATE: dict[tuple[int, int], list[Artist]] = {
    # January
    (1, 1): [
        Artist("Hank Williams", 1923, "American folk art", "country music imagery with rural American scenes"),
        Artist("Satyajit Ray", 1921, "Indian parallel cinema", "Bengali neorealism and humanist storytelling"),
        Artist("J.D. Salinger", 1919, "American literary", "Catcher in the Rye and adolescent alienation"),
    ],
    (1, 2): [
        Artist("Isaac Asimov", 1920, "retrofuturism", "science fiction and space age imagery"),
        Artist("Taye Diggs", 1971, "Broadway theatrical", "contemporary musical theater"),
        Artist("Renata Tebaldi", 1922, "Italian opera", "bel canto and La Scala grandeur"),
    ],
    (1, 3): [
        Artist("Sergio Leone", 1929, "cinematic western", "dramatic wide shots and spaghetti western aesthetics"),
        Artist("Mel Gibson", 1956, "epic cinema", "Braveheart historical drama"),
        Artist("J.R.R. Tolkien", 1892, "high fantasy", "Middle-earth landscapes and elvish wonder"),
    ],
    (1, 4): [
        Artist("Jacob Grimm", 1785, "dark fairy tale illustration", "Germanic folklore and enchanted forest scenes"),
        Artist("Louis Braille", 1809, "tactile innovation", "accessibility and enlightenment imagery"),
        Artist("Isaac Newton", 1643, "scientific enlightenment", "optics, gravity, and natural philosophy"),
    ],
    (1, 5): [
        Artist("Hayao Miyazaki", 1941, "Studio Ghibli anime", "whimsical Japanese animation with nature spirits"),
        Artist("Umberto Eco", 1932, "literary semiotics", "medieval mystery and Name of the Rose"),
        Artist("Diane Keaton", 1946, "New Hollywood", "Annie Hall neurotic charm"),
    ],
    (1, 6): [
        Artist("Gustave Doré", 1832, "detailed engraving", "dramatic biblical and literary illustrations"),
        Artist("Khalil Gibran", 1883, "mystical poetry", "The Prophet and Lebanese spiritual art"),
        Artist("Joan of Arc", 1412, "medieval heroism", "French martyr and warrior saint imagery"),
    ],
    (1, 7): [
        Artist("Charles Addams", 1912, "gothic cartoon", "macabre humor with Victorian gothic elements"),
        Artist("Nicolas Cage", 1964, "intense cinema", "maximalist acting and wild genre films"),
        Artist("Zora Neale Hurston", 1891, "Harlem Renaissance", "Their Eyes Were Watching God and folklore"),
    ],
    (1, 8): [
        Artist("Elvis Presley", 1935, "1950s rock and roll", "vintage Americana and rockabilly aesthetics"),
        Artist("David Bowie", 1947, "glam rock", "Ziggy Stardust and chameleon personas"),
        Artist("Stephen Hawking", 1942, "cosmic physics", "black holes and Brief History of Time"),
    ],
    (1, 9): [
        Artist("Simone de Beauvoir", 1908, "existentialist", "Parisian intellectual and feminist imagery"),
        Artist("Richard Nixon", 1913, "Cold War era", "1970s political drama and Watergate"),
        Artist("Kate Middleton", 1982, "British royal", "contemporary royal elegance"),
    ],
    (1, 10): [
        Artist("Barbara Hepworth", 1903, "modernist sculpture", "organic abstract forms with pierced shapes"),
        Artist("Rod Stewart", 1945, "rock balladry", "raspy vocals and 1970s rock glamour"),
        Artist("Ray Bolger", 1904, "musical theater", "Wizard of Oz scarecrow dance"),
    ],
    (1, 11): [
        Artist("Mary J. Blige", 1971, "urban soul", "contemporary R&B and hip-hop street style"),
        Artist("Alexander Hamilton", 1755, "Founding Fathers", "Federalist Papers and American finance"),
        Artist("Naomi Judd", 1946, "country music", "mother-daughter duo and Nashville"),
    ],
    (1, 12): [
        Artist("John Singer Sargent", 1856, "impressionist portraiture", "elegant society portraits with loose brushwork"),
        Artist("Jack London", 1876, "adventure naturalism", "Call of the Wild and Klondike"),
        Artist("Haruki Murakami", 1949, "magical realism", "surreal Japanese contemporary fiction"),
    ],
    (1, 13): [
        Artist("Orlando Bloom", 1977, "fantasy epic", "Lord of the Rings elvish and medieval fantasy"),
        Artist("Michael Bond", 1926, "children's illustration", "Paddington Bear and London whimsy"),
        Artist("Sophie Tucker", 1886, "vaudeville", "Last of the Red Hot Mamas jazz age"),
    ],
    (1, 14): [
        Artist("Berthe Morisot", 1841, "French Impressionism", "soft domestic scenes with luminous brushwork"),
        Artist("Albert Schweitzer", 1875, "humanitarian", "African missionary and organ music"),
        Artist("Faye Dunaway", 1941, "New Hollywood", "Bonnie and Clyde and Network intensity"),
    ],
    (1, 15): [
        Artist("Martin Luther King Jr.", 1929, "civil rights iconography", "powerful protest imagery and hope symbolism"),
        Artist("Molière", 1622, "French comedy", "Tartuffe and theatrical satire"),
        Artist("Aristotle Onassis", 1906, "jet set glamour", "Greek tycoon and yacht lifestyle"),
    ],
    (1, 16): [
        Artist("Johannes Vermeer", 1632, "Dutch Golden Age", "intimate interior scenes with soft natural light"),
        Artist("Susan Sontag", 1933, "critical theory", "intellectual photography and cultural criticism"),
        Artist("Ethel Merman", 1908, "Broadway belting", "show-stopping musical theater"),
    ],
    (1, 17): [
        Artist("Anne Brontë", 1820, "Victorian romanticism", "moody English moors and Gothic romance"),
        Artist("Benjamin Franklin", 1706, "American Enlightenment", "inventor and founding father imagery"),
        Artist("Muhammad Ali", 1942, "athletic greatness", "boxing champion and cultural icon"),
    ],
    (1, 18): [
        Artist("A.A. Milne", 1882, "children's book illustration", "Hundred Acre Wood and gentle watercolor whimsy"),
        Artist("Cary Grant", 1904, "classic Hollywood", "debonair leading man elegance"),
        Artist("Kevin Costner", 1955, "American epic", "Dances with Wolves and Field of Dreams"),
    ],
    (1, 19): [
        Artist("Edgar Allan Poe", 1809, "dark romanticism", "Gothic horror with ravens and macabre imagery"),
        Artist("Janis Joplin", 1943, "psychedelic rock", "raw blues and 1960s counterculture"),
        Artist("Robert E. Lee", 1807, "Civil War", "Confederate general and Southern imagery"),
    ],
    (1, 20): [
        Artist("Federico Fellini", 1920, "Italian surrealist cinema", "dreamlike circus and carnival imagery"),
        Artist("David Lynch", 1946, "surrealist cinema", "Twin Peaks and nightmarish Americana"),
        Artist("Buzz Aldrin", 1930, "space exploration", "lunar landing and astronaut heroism"),
    ],
    (1, 21): [
        Artist("Christian Dior", 1905, "haute couture fashion", "elegant 1950s New Look fashion illustration"),
        Artist("Placido Domingo", 1941, "operatic tenor", "Three Tenors and Spanish passion"),
        Artist("Geena Davis", 1956, "feminist cinema", "Thelma and Louise empowerment"),
    ],
    (1, 22): [
        Artist("Francis Bacon", 1561, "philosophical allegory", "Renaissance scientific and philosophical imagery"),
        Artist("Lord Byron", 1788, "English Romanticism", "brooding poetry and Mediterranean exile"),
        Artist("D.W. Griffith", 1875, "silent film pioneer", "Birth of a Nation and cinematic language"),
    ],
    (1, 23): [
        Artist("Édouard Manet", 1832, "Impressionist pioneer", "bold modern life scenes breaking academic tradition"),
        Artist("Django Reinhardt", 1910, "Gypsy jazz", "Romani guitar virtuosity"),
        Artist("Jeanne Moreau", 1928, "French New Wave", "Jules et Jim and intellectual glamour"),
    ],
    (1, 24): [
        Artist("Edith Wharton", 1862, "Gilded Age elegance", "opulent American aristocratic interiors"),
        Artist("Neil Diamond", 1941, "pop balladry", "Sweet Caroline and showman sequins"),
        Artist("Sharon Tate", 1943, "1960s Hollywood", "Valley of the Dolls and tragic beauty"),
    ],
    (1, 25): [
        Artist("Robert Burns", 1759, "Scottish romanticism", "Highland landscapes and Celtic folklore"),
        Artist("Virginia Woolf", 1882, "modernist literature", "stream of consciousness and Bloomsbury"),
        Artist("Alicia Keys", 1981, "neo-soul", "piano-driven R&B and empowerment"),
    ],
    (1, 26): [
        Artist("Paul Newman", 1925, "classic Hollywood", "1960s American cinema golden age aesthetics"),
        Artist("Angela Davis", 1944, "Black Power", "revolutionary activism and Afro imagery"),
        Artist("Ellen DeGeneres", 1958, "comedy", "daytime talk and LGBTQ representation"),
    ],
    (1, 27): [
        Artist("Wolfgang Amadeus Mozart", 1756, "Rococo", "18th century Viennese elegance and musical motifs"),
        Artist("Lewis Carroll", 1832, "Victorian fantasy", "Alice in Wonderland surreal whimsy"),
        Artist("Donna Reed", 1921, "1950s television", "It's a Wonderful Life and domestic warmth"),
    ],
    (1, 28): [
        Artist("Jackson Pollock", 1912, "abstract expressionism", "energetic drip paintings with chaotic beauty"),
        Artist("Colette", 1873, "Belle Époque", "Gigi and Parisian sensuality"),
        Artist("Alan Alda", 1936, "television drama", "M*A*S*H and humanist comedy"),
    ],
    (1, 29): [
        Artist("Anton Chekhov", 1860, "Russian realism", "melancholic Russian provincial life scenes"),
        Artist("Oprah Winfrey", 1954, "media empire", "talk show and self-improvement culture"),
        Artist("W.C. Fields", 1880, "vaudeville comedy", "curmudgeon humor and sight gags"),
    ],
    (1, 30): [
        Artist("Franklin D. Roosevelt", 1882, "New Deal era", "1930s-40s American optimism and WPA murals"),
        Artist("Gene Hackman", 1930, "New Hollywood", "French Connection and everyman intensity"),
        Artist("Phil Collins", 1951, "1980s pop rock", "Genesis and solo drums-driven hits"),
    ],
    (1, 31): [
        Artist("Franz Schubert", 1797, "Viennese Romanticism", "Austrian romantic landscapes and lieder imagery"),
        Artist("Norman Mailer", 1923, "New Journalism", "Armies of the Night and machismo prose"),
        Artist("Jackie Robinson", 1919, "baseball integration", "Brooklyn Dodgers and civil rights sports"),
    ],

    # February
    (2, 1): [
        Artist("Langston Hughes", 1902, "Harlem Renaissance", "jazz age African American cultural imagery"),
        Artist("Clark Gable", 1901, "golden age Hollywood", "Gone with the Wind leading man"),
        Artist("Boris Yeltsin", 1931, "post-Soviet Russia", "Kremlin and democratic transition"),
    ],
    (2, 2): [
        Artist("Ayn Rand", 1905, "Art Deco modernism", "heroic individualism and skyscraper architecture"),
        Artist("James Joyce", 1882, "literary modernism", "Ulysses and stream of consciousness Dublin"),
        Artist("Shakira", 1977, "Latin pop", "Colombian hip-shaking and world music fusion"),
    ],
    (2, 3): [
        Artist("Norman Rockwell", 1894, "American illustration", "heartwarming everyday American life scenes"),
        Artist("Gertrude Stein", 1874, "Lost Generation", "Parisian salon and modernist prose"),
        Artist("Felix Mendelssohn", 1809, "German Romanticism", "Wedding March and pastoral elegance"),
    ],
    (2, 4): [
        Artist("Fernand Léger", 1881, "tubular Cubism", "mechanical forms and bold primary colors"),
        Artist("Rosa Parks", 1913, "civil rights icon", "bus boycott and quiet dignity"),
        Artist("Charles Lindbergh", 1902, "aviation pioneer", "Spirit of St. Louis and transatlantic"),
    ],
    (2, 5): [
        Artist("William S. Burroughs", 1914, "Beat Generation", "cut-up technique collage and counterculture"),
        Artist("Hank Aaron", 1934, "baseball legend", "home run king and athletic grace"),
        Artist("Jennifer Jason Leigh", 1962, "indie cinema", "intense character transformation"),
    ],
    (2, 6): [
        Artist("Gustav Klimt", 1862, "Vienna Secession", "golden Byzantine-inspired decorative patterns"),
        Artist("Bob Marley", 1945, "reggae", "Jamaican roots and Rastafarian spirituality"),
        Artist("Ronald Reagan", 1911, "Hollywood to White House", "1980s conservatism and cowboy imagery"),
    ],
    (2, 7): [
        Artist("Charles Dickens", 1812, "Victorian narrative", "foggy London streets and social realism"),
        Artist("Sinclair Lewis", 1885, "American satire", "Main Street and Babbitt social criticism"),
        Artist("Garth Brooks", 1962, "country pop", "stadium country and Oklahoma roots"),
    ],
    (2, 8): [
        Artist("Mary I of England", 1516, "Tudor portraiture", "Renaissance English royal court imagery"),
        Artist("Jules Verne", 1828, "scientific adventure", "20,000 Leagues and Victorian exploration"),
        Artist("John Williams", 1932, "film scoring", "Star Wars and Indiana Jones orchestral"),
    ],
    (2, 9): [
        Artist("Alice Walker", 1944, "Southern Gothic", "African American rural South narratives"),
        Artist("Carole King", 1942, "singer-songwriter", "Tapestry and 1970s confessional pop"),
        Artist("Mia Farrow", 1945, "art house cinema", "Rosemary's Baby and Woody Allen muse"),
    ],
    (2, 10): [
        Artist("Boris Pasternak", 1890, "Russian symbolism", "Doctor Zhivago winter landscapes"),
        Artist("Bertolt Brecht", 1898, "epic theater", "Threepenny Opera and alienation effect"),
        Artist("Laura Dern", 1967, "auteur cinema", "David Lynch muse and character depth"),
    ],
    (2, 11): [
        Artist("Thomas Edison", 1847, "industrial innovation", "Victorian invention and early electric age"),
        Artist("Burt Reynolds", 1936, "1970s machismo", "Smokey and the Bandit and mustache"),
        Artist("Jennifer Aniston", 1969, "sitcom to cinema", "Friends and romantic comedy"),
    ],
    (2, 12): [
        Artist("Abraham Lincoln", 1809, "Civil War era", "19th century American history and emancipation"),
        Artist("Charles Darwin", 1809, "natural history", "evolution and Beagle expedition"),
        Artist("Judy Blume", 1938, "young adult fiction", "coming-of-age and adolescent honesty"),
    ],
    (2, 13): [
        Artist("Georges Simenon", 1903, "noir detective", "rain-soaked Paris and moody crime scenes"),
        Artist("Chuck Yeager", 1923, "aviation", "breaking sound barrier and test pilot"),
        Artist("Peter Gabriel", 1950, "art rock", "Genesis and world music fusion"),
    ],
    (2, 14): [
        Artist("Frederick Douglass", 1818, "abolitionist", "powerful anti-slavery and dignity imagery"),
        Artist("Carl Bernstein", 1944, "investigative journalism", "Watergate and All the President's Men"),
        Artist("Michael Bloomberg", 1942, "media and politics", "New York City and financial data"),
    ],
    (2, 15): [
        Artist("Galileo Galilei", 1564, "Renaissance astronomy", "celestial maps and scientific discovery"),
        Artist("Susan B. Anthony", 1820, "suffrage movement", "women's rights and equality"),
        Artist("Matt Groening", 1954, "animation satire", "Simpsons and yellow-skinned Americana"),
    ],
    (2, 16): [
        Artist("LeVar Burton", 1957, "educational media", "Reading Rainbow wonder and Star Trek cosmos"),
        Artist("Sonny Bono", 1935, "1960s pop duo", "Sonny and Cher variety show"),
        Artist("Ice-T", 1958, "gangsta rap", "West Coast hip-hop and Law & Order"),
    ],
    (2, 17): [
        Artist("Yoko Ono", 1933, "Fluxus conceptual art", "minimalist peace activism and avant-garde"),
        Artist("Michael Jordan", 1963, "basketball greatness", "Air Jordan and athletic excellence"),
        Artist("Huey Newton", 1942, "Black Panther Party", "revolutionary imagery and social justice"),
    ],
    (2, 18): [
        Artist("Toni Morrison", 1931, "African American literature", "Beloved and magical historical fiction"),
        Artist("Enzo Ferrari", 1898, "automotive design", "red racing cars and Italian speed"),
        Artist("John Travolta", 1954, "disco era", "Saturday Night Fever and Grease"),
    ],
    (2, 19): [
        Artist("Nicolaus Copernicus", 1473, "heliocentric astronomy", "Renaissance scientific revolution imagery"),
        Artist("Smokey Robinson", 1940, "Motown", "silky soul and Miracles harmony"),
        Artist("Jeff Daniels", 1955, "character acting", "Dumb and Dumber to Newsroom range"),
    ],
    (2, 20): [
        Artist("Ansel Adams", 1902, "landscape photography", "dramatic black and white American wilderness"),
        Artist("Kurt Cobain", 1967, "grunge rock", "Nirvana and 1990s Seattle angst"),
        Artist("Gloria Vanderbilt", 1924, "fashion and society", "jeans and American aristocracy"),
    ],
    (2, 21): [
        Artist("Nina Simone", 1933, "jazz and blues", "soulful African American musical expression"),
        Artist("W.H. Auden", 1907, "modernist poetry", "intellectual verse and English elegance"),
        Artist("Anais Nin", 1903, "erotic literature", "diary and feminine sensuality"),
    ],
    (2, 22): [
        Artist("George Washington", 1732, "American Federal", "colonial American and revolutionary imagery"),
        Artist("Frederic Chopin", 1810, "Romantic piano", "nocturnes and Polish melancholy"),
        Artist("Drew Barrymore", 1975, "Hollywood royalty", "E.T. to rom-com leading lady"),
    ],
    (2, 23): [
        Artist("W.E.B. Du Bois", 1868, "Pan-African", "intellectual African American heritage"),
        Artist("George Frideric Handel", 1685, "Baroque grandeur", "Messiah and oratorio splendor"),
        Artist("Aziz Ansari", 1983, "contemporary comedy", "Master of None and modern romance"),
    ],
    (2, 24): [
        Artist("Winslow Homer", 1836, "American realism", "dramatic seascapes and Civil War scenes"),
        Artist("Steve Jobs", 1955, "digital design", "Apple aesthetics and minimalist tech"),
        Artist("Floyd Patterson", 1935, "boxing", "heavyweight champion dignity"),
    ],
    (2, 25): [
        Artist("Pierre-Auguste Renoir", 1841, "French Impressionism", "joyful sun-dappled social gatherings"),
        Artist("George Harrison", 1943, "Beatles spirituality", "Indian influences and quiet guitar"),
        Artist("Rashida Jones", 1976, "comedy television", "Parks and Recreation and modern charm"),
    ],
    (2, 26): [
        Artist("Victor Hugo", 1802, "French Romanticism", "dramatic Gothic architecture and revolution"),
        Artist("Buffalo Bill", 1846, "Wild West show", "frontier spectacle and cowboy legend"),
        Artist("Johnny Cash", 1932, "country outlaw", "Man in Black and American roots"),
    ],
    (2, 27): [
        Artist("John Steinbeck", 1902, "American social realism", "Dust Bowl and California migrant imagery"),
        Artist("Elizabeth Taylor", 1932, "Hollywood glamour", "violet eyes and Cleopatra excess"),
        Artist("Ralph Nader", 1934, "consumer advocacy", "Unsafe at Any Speed and activism"),
    ],
    (2, 28): [
        Artist("Linus Pauling", 1901, "molecular structure", "scientific chemistry and peace activism"),
        Artist("Zero Mostel", 1915, "theatrical comedy", "Fiddler on the Roof and big personality"),
        Artist("Bernadette Peters", 1948, "Broadway star", "Sondheim and curly-haired glamour"),
    ],
    (2, 29): [
        Artist("Gioacchino Rossini", 1792, "Italian opera", "theatrical Romantic era musical drama"),
        Artist("Jimmy Dorsey", 1904, "big band", "swing era and saxophone"),
        Artist("Tony Robbins", 1960, "motivational", "self-help and empowerment imagery"),
    ],

    # March
    (3, 1): [
        Artist("Frédéric Chopin", 1810, "Romantic piano", "Polish nocturnes and melancholic elegance"),
        Artist("Glenn Miller", 1904, "big band swing", "In the Mood and WWII dance"),
        Artist("Ron Howard", 1954, "mainstream cinema", "Happy Days to A Beautiful Mind"),
    ],
    (3, 2): [
        Artist("Dr. Seuss", 1904, "whimsical illustration", "fantastical creatures and playful surrealism"),
        Artist("Lou Reed", 1942, "art rock", "Velvet Underground and New York grit"),
        Artist("Tom Wolfe", 1930, "New Journalism", "Bonfire of Vanities and white suits"),
    ],
    (3, 3): [
        Artist("Alexander Graham Bell", 1847, "Victorian invention", "early telecommunications and innovation"),
        Artist("Jean Harlow", 1911, "pre-Code Hollywood", "platinum blonde bombshell"),
        Artist("Jessica Biel", 1982, "contemporary cinema", "athletic beauty and action"),
    ],
    (3, 4): [
        Artist("Miriam Makeba", 1932, "African music", "South African anti-apartheid and world music"),
        Artist("Antonio Vivaldi", 1678, "Baroque", "Four Seasons and Venetian strings"),
        Artist("Chaz Bono", 1969, "LGBTQ advocacy", "transgender visibility and courage"),
    ],
    (3, 5): [
        Artist("Pier Paolo Pasolini", 1922, "Italian neorealism", "stark social commentary and classical myth"),
        Artist("Howard Pyle", 1853, "adventure illustration", "pirates and medieval romance"),
        Artist("Andy Gibb", 1958, "disco pop", "teen idol and Bee Gees brother"),
    ],
    (3, 6): [
        Artist("Michelangelo", 1475, "High Renaissance", "powerful human forms and Sistine Chapel grandeur"),
        Artist("Gabriel García Márquez", 1927, "magical realism", "One Hundred Years of Solitude"),
        Artist("Elizabeth Barrett Browning", 1806, "Victorian poetry", "Sonnets from the Portuguese romance"),
    ],
    (3, 7): [
        Artist("Piet Mondrian", 1872, "De Stijl", "primary color grids and geometric abstraction"),
        Artist("Maurice Ravel", 1875, "Impressionist music", "Bolero and orchestral color"),
        Artist("Bryan Cranston", 1956, "prestige television", "Breaking Bad transformation"),
    ],
    (3, 8): [
        Artist("Oliver Wendell Holmes Jr.", 1841, "legal philosophy", "American jurisprudence and wisdom"),
        Artist("Aidan Quinn", 1959, "character acting", "intense dramatic roles"),
        Artist("Cyd Charisse", 1922, "MGM musicals", "long-legged dance elegance"),
    ],
    (3, 9): [
        Artist("Yuri Gagarin", 1934, "Soviet space age", "cosmonaut and early space exploration imagery"),
        Artist("Amerigo Vespucci", 1454, "Age of Exploration", "New World cartography"),
        Artist("Juliette Binoche", 1964, "French cinema", "Three Colors and European art film"),
    ],
    (3, 10): [
        Artist("Harriet Tubman", 1822, "Underground Railroad", "freedom and abolitionist courage"),
        Artist("Sharon Stone", 1958, "1990s cinema", "Basic Instinct and femme fatale"),
        Artist("Chuck Norris", 1940, "martial arts action", "Walker Texas Ranger and meme legend"),
    ],
    (3, 11): [
        Artist("Douglas Adams", 1952, "science fiction comedy", "Hitchhiker's Guide absurdist space humor"),
        Artist("Bobby McFerrin", 1950, "vocal jazz", "Don't Worry Be Happy and acapella"),
        Artist("Thora Birch", 1982, "indie cinema", "Ghost World and American Beauty"),
    ],
    (3, 12): [
        Artist("Jack Kerouac", 1922, "Beat Generation", "On the Road American highway and jazz"),
        Artist("Liza Minnelli", 1946, "Cabaret glamour", "Broadway and Hollywood musical star"),
        Artist("James Taylor", 1948, "singer-songwriter", "Fire and Rain acoustic folk"),
    ],
    (3, 13): [
        Artist("L. Ron Hubbard", 1911, "pulp science fiction", "1930s-40s sci-fi magazine cover art"),
        Artist("Neil Sedaka", 1939, "1960s pop", "Calendar Girl and Brill Building"),
        Artist("William H. Macy", 1950, "character acting", "Fargo and Shameless everyman"),
    ],
    (3, 14): [
        Artist("Albert Einstein", 1879, "scientific visualization", "relativity and cosmic space-time"),
        Artist("Billy Crystal", 1948, "comedy", "When Harry Met Sally and Oscar hosting"),
        Artist("Quincy Jones", 1933, "music production", "Thriller and jazz orchestration"),
    ],
    (3, 15): [
        Artist("Ruth Bader Ginsburg", 1933, "judicial iconography", "justice and equality symbolism"),
        Artist("Andrew Jackson", 1767, "Jacksonian America", "Old Hickory and frontier democracy"),
        Artist("will.i.am", 1975, "hip-hop production", "Black Eyed Peas and futuristic beats"),
    ],
    (3, 16): [
        Artist("Rosa Bonheur", 1822, "animal painting", "majestic horses and rural livestock realism"),
        Artist("Jerry Lewis", 1926, "slapstick comedy", "nutty professor and telethon"),
        Artist("Alexandra Daddario", 1986, "contemporary cinema", "striking blue eyes and genre work"),
    ],
    (3, 17): [
        Artist("Nat King Cole", 1919, "golden age jazz", "elegant 1950s crooner and supper club"),
        Artist("Rob Lowe", 1964, "Brat Pack", "1980s heartthrob to Parks and Rec"),
        Artist("Kurt Russell", 1951, "action cinema", "Escape from New York and Disney child star"),
    ],
    (3, 18): [
        Artist("Nikolai Rimsky-Korsakov", 1844, "Russian orchestral", "Scheherazade and fairy tale operas"),
        Artist("John Updike", 1932, "American suburban", "Rabbit novels and literary realism"),
        Artist("Queen Latifah", 1970, "hip-hop to Hollywood", "rap royalty and acting range"),
    ],
    (3, 19): [
        Artist("Frédéric Joliot-Curie", 1900, "atomic age", "nuclear science and mid-century research"),
        Artist("Philip Roth", 1933, "American literary", "Portnoy and Jewish-American experience"),
        Artist("Bruce Willis", 1955, "action cinema", "Die Hard and everyman hero"),
    ],
    (3, 20): [
        Artist("Ovid", 43, "classical mythology", "Metamorphoses and ancient Roman tales"),
        Artist("Henrik Ibsen", 1828, "modern drama", "Doll's House and social realism"),
        Artist("Spike Lee", 1957, "Black cinema", "Do the Right Thing and Brooklyn"),
    ],
    (3, 21): [
        Artist("Johann Sebastian Bach", 1685, "Baroque", "complex musical structures and cathedral grandeur"),
        Artist("Gary Oldman", 1958, "character transformation", "chameleon acting and villain roles"),
        Artist("Rosie O'Donnell", 1962, "talk show comedy", "daytime television and Broadway"),
    ],
    (3, 22): [
        Artist("Marcel Marceau", 1923, "mime art", "silent performance and French pantomime"),
        Artist("Stephen Sondheim", 1930, "musical theater genius", "Sweeney Todd and Into the Woods"),
        Artist("Reese Witherspoon", 1976, "Hollywood producer", "Legally Blonde to Big Little Lies"),
    ],
    (3, 23): [
        Artist("Akira Kurosawa", 1910, "Japanese cinema", "samurai epics and dynamic compositions"),
        Artist("Joan Crawford", 1904, "Hollywood diva", "Mildred Pierce and studio era glamour"),
        Artist("Keri Russell", 1976, "television drama", "Felicity hair and The Americans spy"),
    ],
    (3, 24): [
        Artist("William Morris", 1834, "Arts and Crafts", "intricate floral patterns and medieval revival"),
        Artist("Harry Houdini", 1874, "escape artistry", "magic and Victorian spectacle"),
        Artist("Steve McQueen", 1930, "cool cinema", "Bullitt and King of Cool"),
    ],
    (3, 25): [
        Artist("Aretha Franklin", 1942, "soul music", "powerful gospel and R&B expression"),
        Artist("Flannery O'Connor", 1925, "Southern Gothic", "grotesque and Catholic grace"),
        Artist("Elton John", 1947, "glam rock", "piano man and outrageous costumes"),
    ],
    (3, 26): [
        Artist("Robert Frost", 1874, "New England poetry", "rural American landscapes and nature"),
        Artist("Tennessee Williams", 1911, "Southern drama", "Streetcar Named Desire and passion"),
        Artist("Diana Ross", 1944, "Motown glamour", "Supremes and solo diva"),
    ],
    (3, 27): [
        Artist("Ludwig Mies van der Rohe", 1886, "International Style architecture", "minimalist glass and steel"),
        Artist("Quentin Tarantino", 1963, "postmodern cinema", "Pulp Fiction and cinephile violence"),
        Artist("Mariah Carey", 1969, "vocal acrobatics", "five-octave range and Christmas"),
    ],
    (3, 28): [
        Artist("Fra Bartolomeo", 1472, "High Renaissance", "religious devotional paintings and sfumato"),
        Artist("Reba McEntire", 1955, "country music", "red-haired Nashville queen"),
        Artist("Lady Gaga", 1986, "pop art performance", "meat dress and monster aesthetic"),
    ],
    (3, 29): [
        Artist("John Tyler", 1790, "early American", "antebellum Southern plantation era"),
        Artist("Walt Frazier", 1945, "basketball style", "Clyde and 1970s Knicks cool"),
        Artist("Lucy Lawless", 1968, "action television", "Xena Warrior Princess strength"),
    ],
    (3, 30): [
        Artist("Vincent van Gogh", 1853, "Post-Impressionism", "swirling starry nights and vibrant colors"),
        Artist("Francisco Goya", 1746, "Spanish Romanticism", "dark Saturn and royal portraits"),
        Artist("Celine Dion", 1968, "power ballads", "Titanic and vocal grandeur"),
    ],
    (3, 31): [
        Artist("Joseph Haydn", 1732, "Classical era", "elegant 18th century symphonic refinement"),
        Artist("Descartes", 1596, "philosophical rationalism", "I think therefore I am"),
        Artist("Ewan McGregor", 1971, "versatile cinema", "Trainspotting to Obi-Wan"),
    ],

    # April
    (4, 1): [
        Artist("Sergei Rachmaninoff", 1873, "Russian Romanticism", "sweeping emotional piano and orchestral"),
        Artist("Debbie Reynolds", 1932, "MGM musicals", "Singin' in the Rain and Hollywood mom"),
        Artist("Ali MacGraw", 1939, "1970s cinema", "Love Story and bohemian style"),
    ],
    (4, 2): [
        Artist("Hans Christian Andersen", 1805, "fairy tale illustration", "Little Mermaid and enchanted stories"),
        Artist("Marvin Gaye", 1939, "soul music", "What's Going On and Motown sensuality"),
        Artist("Emmylou Harris", 1947, "country rock", "silver hair and cosmic American music"),
    ],
    (4, 3): [
        Artist("Eddie Murphy", 1961, "1980s comedy", "Beverly Hills Cop and vibrant pop culture"),
        Artist("Doris Day", 1922, "wholesome Hollywood", "pillow talk and sunny optimism"),
        Artist("Alec Baldwin", 1958, "dramatic range", "Glengarry Glen Ross to 30 Rock"),
    ],
    (4, 4): [
        Artist("Maya Angelou", 1928, "African American literature", "caged bird and resilient hope imagery"),
        Artist("Robert Downey Jr.", 1965, "Hollywood comeback", "Iron Man and charisma"),
        Artist("Anthony Perkins", 1932, "psychological thriller", "Psycho and Norman Bates"),
    ],
    (4, 5): [
        Artist("Booker T. Washington", 1856, "African American education", "Tuskegee and uplift symbolism"),
        Artist("Bette Davis", 1908, "Hollywood grande dame", "All About Eve and fierce eyes"),
        Artist("Colin Powell", 1937, "military leadership", "Desert Storm and statesmanship"),
    ],
    (4, 6): [
        Artist("Raphael", 1483, "High Renaissance", "harmonious composition and Madonna ideals"),
        Artist("Merle Haggard", 1937, "outlaw country", "Okie from Muskogee and working class"),
        Artist("Paul Rudd", 1969, "comedy everyman", "Ant-Man and eternal youth"),
    ],
    (4, 7): [
        Artist("Francis Ford Coppola", 1939, "New Hollywood cinema", "Godfather and Apocalypse Now imagery"),
        Artist("Billie Holiday", 1915, "jazz torch singer", "Strange Fruit and melancholy beauty"),
        Artist("Jackie Chan", 1954, "martial arts comedy", "Hong Kong stunts and physical comedy"),
    ],
    (4, 8): [
        Artist("Kofi Annan", 1938, "diplomatic", "United Nations and global peace"),
        Artist("Betty Ford", 1918, "first lady candor", "addiction recovery and openness"),
        Artist("Patricia Arquette", 1968, "indie cinema", "Boyhood and True Romance"),
    ],
    (4, 9): [
        Artist("Charles Baudelaire", 1821, "French Symbolism", "Flowers of Evil and decadent poetry"),
        Artist("Hugh Hefner", 1926, "Playboy aesthetic", "bachelor pad and mid-century cool"),
        Artist("Dennis Quaid", 1954, "Hollywood leading man", "versatile American actor"),
    ],
    (4, 10): [
        Artist("Joseph Pulitzer", 1847, "yellow journalism", "newspaper era and press illustration"),
        Artist("Omar Sharif", 1932, "international cinema", "Doctor Zhivago and exotic romance"),
        Artist("Mandy Moore", 1984, "teen pop to drama", "This Is Us and pop singer"),
    ],
    (4, 11): [
        Artist("Louise Bourgeois", 1911, "confessional sculpture", "giant spiders and psychological art"),
        Artist("Joel Grey", 1932, "Cabaret emcee", "willkommen and theatrical magic"),
        Artist("Joss Stone", 1987, "blue-eyed soul", "British R&B and powerful vocals"),
    ],
    (4, 12): [
        Artist("Beverly Cleary", 1916, "children's book illustration", "Ramona Quimby neighborhood stories"),
        Artist("David Letterman", 1947, "late night television", "ironic comedy and gap teeth"),
        Artist("Andy Garcia", 1956, "Cuban-American cinema", "Godfather III and suave intensity"),
    ],
    (4, 13): [
        Artist("Thomas Jefferson", 1743, "Neoclassical", "American founding and Monticello architecture"),
        Artist("Seamus Heaney", 1939, "Irish poetry", "Nobel laureate and earthy verse"),
        Artist("Al Green", 1946, "soul music", "Let's Stay Together and gospel warmth"),
    ],
    (4, 14): [
        Artist("Anne Sullivan", 1866, "educational", "Helen Keller and breakthrough communication"),
        Artist("Pete Rose", 1941, "baseball", "Charlie Hustle and Cincinnati Reds"),
        Artist("Loretta Lynn", 1932, "country music", "Coal Miner's Daughter and Appalachia"),
    ],
    (4, 15): [
        Artist("Leonardo da Vinci", 1452, "Renaissance polymath", "anatomical drawings and Mona Lisa mastery"),
        Artist("Emma Watson", 1990, "Harry Potter generation", "Hermione and feminist advocacy"),
        Artist("Bessie Smith", 1894, "classic blues", "Empress of the Blues and raw power"),
    ],
    (4, 16): [
        Artist("Charlie Chaplin", 1889, "silent film", "Little Tramp and black-white cinema comedy"),
        Artist("Kareem Abdul-Jabbar", 1947, "basketball greatness", "sky hook and intellectual athlete"),
        Artist("Ellen Barkin", 1954, "character actress", "sultry intensity and New York edge"),
    ],
    (4, 17): [
        Artist("Isak Dinesen", 1885, "African colonial", "Out of Africa and Danish literary art"),
        Artist("Thornton Wilder", 1897, "American theater", "Our Town and small-town wisdom"),
        Artist("Victoria Beckham", 1974, "Spice Girls to fashion", "Posh and designer evolution"),
    ],
    (4, 18): [
        Artist("Leopold Stokowski", 1882, "orchestral conducting", "Fantasia and symphonic visualization"),
        Artist("Hayley Mills", 1946, "Disney childhood", "Parent Trap and British charm"),
        Artist("Kourtney Kardashian", 1979, "reality television", "lifestyle and family dynasty"),
    ],
    (4, 19): [
        Artist("Maria Sharapova", 1987, "athletic dynamism", "tennis and sports photography"),
        Artist("Kate Hudson", 1979, "rom-com charm", "Almost Famous and Hollywood daughter"),
        Artist("Tim Curry", 1946, "theatrical camp", "Rocky Horror and character roles"),
    ],
    (4, 20): [
        Artist("Joan Miró", 1893, "surrealist abstraction", "biomorphic shapes and bold primary colors"),
        Artist("Adolf Hitler", 1889, "failed artist", "watercolors and Vienna rejection"),
        Artist("Carmen Electra", 1972, "1990s pop culture", "Baywatch and MTV"),
    ],
    (4, 21): [
        Artist("Charlotte Brontë", 1816, "Victorian Gothic", "Jane Eyre moors and passionate romance"),
        Artist("Queen Elizabeth II", 1926, "British monarchy", "coronation and royal duty"),
        Artist("Iggy Pop", 1947, "punk rock", "Stooges and shirtless stage diving"),
    ],
    (4, 22): [
        Artist("Immanuel Kant", 1724, "Enlightenment philosophy", "German philosophical and cosmic imagery"),
        Artist("Jack Nicholson", 1937, "New Hollywood", "One Flew Over and Joker madness"),
        Artist("John Waters", 1946, "trash cinema", "Pink Flamingos and Baltimore camp"),
    ],
    (4, 23): [
        Artist("William Shakespeare", 1564, "Elizabethan theatre", "Globe Theatre and dramatic storytelling"),
        Artist("Shirley Temple", 1928, "child star", "dimples and Depression-era optimism"),
        Artist("Dev Patel", 1990, "British-Indian cinema", "Slumdog Millionaire breakout"),
    ],
    (4, 24): [
        Artist("Willem de Kooning", 1904, "abstract expressionism", "gestural woman figures and bold strokes"),
        Artist("Barbra Streisand", 1942, "entertainment legend", "Funny Girl and perfectionist diva"),
        Artist("Shirley MacLaine", 1934, "Hollywood mystic", "Terms of Endearment and spirituality"),
    ],
    (4, 25): [
        Artist("Ella Fitzgerald", 1917, "jazz standards", "elegant scat singing and big band era"),
        Artist("Al Pacino", 1940, "Method acting", "Godfather and intense transformation"),
        Artist("Renée Zellweger", 1969, "dramatic range", "Bridget Jones to Chicago"),
    ],
    (4, 26): [
        Artist("Eugene Delacroix", 1798, "French Romanticism", "Liberty Leading the People dramatic color"),
        Artist("I.M. Pei", 1917, "modernist architecture", "Louvre pyramid and geometric elegance"),
        Artist("Carol Burnett", 1933, "variety television", "sketch comedy and versatility"),
    ],
    (4, 27): [
        Artist("Ulysses S. Grant", 1822, "Civil War era", "Union military and Reconstruction"),
        Artist("Coretta Scott King", 1927, "civil rights", "Martin's wife and legacy keeper"),
        Artist("Tina Fey", 1970, "comedy writing", "30 Rock and SNL Weekend Update"),
    ],
    (4, 28): [
        Artist("Harper Lee", 1926, "Southern Gothic", "To Kill a Mockingbird courthouse drama"),
        Artist("Jay Leno", 1950, "late night television", "Tonight Show and car collection"),
        Artist("Jessica Alba", 1981, "Hollywood beauty", "Dark Angel and entrepreneurship"),
    ],
    (4, 29): [
        Artist("Duke Ellington", 1899, "jazz orchestration", "Cotton Club and sophisticated swing"),
        Artist("William Randolph Hearst", 1863, "yellow journalism", "Citizen Kane inspiration"),
        Artist("Uma Thurman", 1970, "auteur muse", "Pulp Fiction and Kill Bill"),
    ],
    (4, 30): [
        Artist("Carl Friedrich Gauss", 1777, "mathematical", "number theory and geometric perfection"),
        Artist("Willie Nelson", 1933, "outlaw country", "braids and On the Road Again"),
        Artist("Kirsten Dunst", 1982, "child star evolution", "Spider-Man and indie drama"),
    ],

    # May
    (5, 1): [
        Artist("Joseph Heller", 1923, "black comedy", "Catch-22 absurdist military satire"),
        Artist("Glenn Ford", 1916, "classic Hollywood", "Gilda and Western leading man"),
        Artist("Tim McGraw", 1967, "country star", "Nashville power couple"),
    ],
    (5, 2): [
        Artist("Catherine the Great", 1729, "Russian Imperial", "Hermitage and Enlightenment grandeur"),
        Artist("Donatello", 1386, "Early Renaissance sculpture", "David and Florentine mastery"),
        Artist("Dwayne Johnson", 1972, "action star", "The Rock and charismatic muscles"),
    ],
    (5, 3): [
        Artist("Niccolò Machiavelli", 1469, "Renaissance political", "The Prince and Florentine intrigue"),
        Artist("Bing Crosby", 1903, "crooner", "White Christmas and easy listening"),
        Artist("Christina Hendricks", 1975, "prestige television", "Mad Men curves and glamour"),
    ],
    (5, 4): [
        Artist("Audrey Hepburn", 1929, "classic Hollywood glamour", "Breakfast at Tiffany's elegance"),
        Artist("Keith Haring", 1958, "pop art", "graffiti figures and AIDS activism"),
        Artist("Will Arnett", 1970, "comedy voice", "Bojack Horseman and GOB Bluth"),
    ],
    (5, 5): [
        Artist("Søren Kierkegaard", 1813, "existentialist", "Danish philosophy and melancholic imagery"),
        Artist("Karl Marx", 1818, "revolutionary politics", "Communist Manifesto and social theory"),
        Artist("Adele", 1988, "vocal power", "Someone Like You and emotional ballads"),
    ],
    (5, 6): [
        Artist("Sigmund Freud", 1856, "psychoanalytic", "dream symbolism and subconscious imagery"),
        Artist("Orson Welles", 1915, "cinema genius", "Citizen Kane and radio drama"),
        Artist("George Clooney", 1961, "Hollywood royalty", "ER to Oceans and activism"),
    ],
    (5, 7): [
        Artist("Pyotr Ilyich Tchaikovsky", 1840, "Russian Romantic ballet", "Swan Lake and Nutcracker magic"),
        Artist("Johannes Brahms", 1833, "German Romanticism", "symphonic grandeur and chamber intimacy"),
        Artist("Eva Perón", 1919, "Argentine glamour", "Evita and Descamisados"),
    ],
    (5, 8): [
        Artist("Jean-Henri Dunant", 1828, "humanitarian", "Red Cross and compassion iconography"),
        Artist("Harry S. Truman", 1884, "atomic age", "postwar America and plain speaking"),
        Artist("Enrique Iglesias", 1975, "Latin pop", "Bailamos and romantic hero"),
    ],
    (5, 9): [
        Artist("Howard Carter", 1874, "Egyptology", "King Tut and ancient Egyptian treasures"),
        Artist("Billy Joel", 1949, "piano man", "New York state of mind and balladry"),
        Artist("Rosario Dawson", 1979, "indie cinema", "Rent and genre versatility"),
    ],
    (5, 10): [
        Artist("Fred Astaire", 1899, "golden age Hollywood", "elegant tap dancing and Art Deco musicals"),
        Artist("Bono", 1960, "rock activism", "U2 and humanitarian rock star"),
        Artist("Sid Vicious", 1957, "punk rock", "Sex Pistols and nihilism"),
    ],
    (5, 11): [
        Artist("Salvador Dalí", 1904, "surrealism", "melting clocks and dreamscape imagery"),
        Artist("Irving Berlin", 1888, "American songbook", "White Christmas and God Bless America"),
        Artist("Natasha Richardson", 1963, "theatrical dynasty", "British acting royalty"),
    ],
    (5, 12): [
        Artist("Florence Nightingale", 1820, "Victorian nursing", "lamp-bearing and medical care imagery"),
        Artist("Katharine Hepburn", 1907, "independent Hollywood", "strong women and four Oscars"),
        Artist("Tony Hawk", 1968, "skateboarding", "900 and extreme sports icon"),
    ],
    (5, 13): [
        Artist("Georges Braque", 1882, "analytic Cubism", "fragmented still lifes and collage"),
        Artist("Stevie Wonder", 1950, "Motown genius", "Superstition and musical innovation"),
        Artist("Stephen Colbert", 1964, "satirical comedy", "Colbert Report and Late Show"),
    ],
    (5, 14): [
        Artist("Mark Zuckerberg", 1984, "digital technology", "social network and Silicon Valley"),
        Artist("George Lucas", 1944, "blockbuster cinema", "Star Wars and American Graffiti"),
        Artist("Cate Blanchett", 1969, "Australian cinema", "Oscar range and ethereal beauty"),
    ],
    (5, 15): [
        Artist("Emily Dickinson", 1830, "American poetry", "reclusive New England and nature verse"),
        Artist("L. Frank Baum", 1856, "fantasy children's", "Wizard of Oz and Emerald City"),
        Artist("Madeleine Albright", 1937, "diplomatic style", "first female Secretary of State pins"),
    ],
    (5, 16): [
        Artist("Liberace", 1919, "glitzy showmanship", "rhinestone costumes and candelabras"),
        Artist("Henry Fonda", 1905, "American cinema", "Grapes of Wrath and moral authority"),
        Artist("Megan Fox", 1986, "Hollywood bombshell", "Transformers and modern pin-up"),
    ],
    (5, 17): [
        Artist("Erik Satie", 1866, "avant-garde minimalism", "Gymnopédies and Parisian whimsy"),
        Artist("Dennis Hopper", 1936, "counterculture cinema", "Easy Rider and artistic rebellion"),
        Artist("Nikki Reed", 1988, "indie cinema", "Thirteen and Twilight"),
    ],
    (5, 18): [
        Artist("Bertrand Russell", 1872, "logical philosophy", "mathematical logic and pacifism"),
        Artist("Pope John Paul II", 1920, "Catholic imagery", "Polish Pope and global travels"),
        Artist("Tina Fey", 1970, "comedy writing", "30 Rock and Mean Girls"),
    ],
    (5, 19): [
        Artist("Malcolm X", 1925, "civil rights", "Black Power and revolutionary imagery"),
        Artist("Nora Ephron", 1941, "romantic comedy", "When Harry Met Sally and wit"),
        Artist("Pete Townshend", 1945, "rock opera", "The Who and windmill guitar"),
    ],
    (5, 20): [
        Artist("Honoré de Balzac", 1799, "French realism", "La Comédie Humaine society scenes"),
        Artist("James Stewart", 1908, "American everyman", "It's a Wonderful Life sincerity"),
        Artist("Cher", 1946, "entertainment chameleon", "fashion icon and Oscar winner"),
    ],
    (5, 21): [
        Artist("Albrecht Dürer", 1471, "Northern Renaissance", "intricate woodcuts and engravings"),
        Artist("Fats Waller", 1904, "stride piano", "Ain't Misbehavin' and jazz wit"),
        Artist("Mr. T", 1952, "1980s action", "A-Team and gold chains"),
    ],
    (5, 22): [
        Artist("Mary Cassatt", 1844, "American Impressionism", "tender mother and child scenes"),
        Artist("Arthur Conan Doyle", 1859, "detective fiction", "Sherlock Holmes and Victorian mystery"),
        Artist("Naomi Campbell", 1970, "supermodel", "runway queen and 1990s fashion"),
    ],
    (5, 23): [
        Artist("Franz Mesmer", 1734, "mesmerism", "hypnotic and mysterious occult imagery"),
        Artist("Margaret Fuller", 1810, "Transcendentalism", "feminist and intellectual activism"),
        Artist("Drew Carey", 1958, "everyman comedy", "Price is Right and improv"),
    ],
    (5, 24): [
        Artist("Bob Dylan", 1941, "folk rock", "protest songs and 1960s counterculture"),
        Artist("Queen Victoria", 1819, "Victorian era", "British Empire and mourning queen"),
        Artist("Priscilla Presley", 1945, "Elvis legacy", "Graceland and Dallas glamour"),
    ],
    (5, 25): [
        Artist("Ralph Waldo Emerson", 1803, "Transcendentalism", "nature philosophy and self-reliance"),
        Artist("Miles Davis", 1926, "jazz innovation", "Kind of Blue and cool jazz"),
        Artist("Ian McKellen", 1939, "Shakespearean cinema", "Gandalf and LGBTQ icon"),
    ],
    (5, 26): [
        Artist("John Wayne", 1907, "classic western", "cowboy frontier and Monument Valley"),
        Artist("Peggy Lee", 1920, "cool jazz", "Fever and sultry vocals"),
        Artist("Lenny Kravitz", 1964, "retro rock", "Are You Gonna Go My Way"),
    ],
    (5, 27): [
        Artist("Isadora Duncan", 1877, "modern dance", "flowing Greek-inspired movement"),
        Artist("Wild Bill Hickok", 1837, "Wild West", "frontier lawman and gunslinger"),
        Artist("Paul Bettany", 1971, "British cinema", "Vision and versatile character work"),
    ],
    (5, 28): [
        Artist("Ian Fleming", 1908, "spy thriller", "James Bond and Cold War espionage"),
        Artist("Gladys Knight", 1944, "soul music", "Midnight Train to Georgia"),
        Artist("Kylie Minogue", 1968, "pop princess", "Australian pop and disco revival"),
    ],
    (5, 29): [
        Artist("John F. Kennedy", 1917, "Camelot era", "1960s American optimism and space race"),
        Artist("Bob Hope", 1903, "comedy legend", "USO tours and Hollywood variety"),
        Artist("Annette Bening", 1958, "dramatic actress", "American Beauty and stage elegance"),
    ],
    (5, 30): [
        Artist("Peter Carl Fabergé", 1846, "decorative arts", "jeweled Easter eggs and Russian luxury"),
        Artist("Benny Goodman", 1909, "swing clarinet", "King of Swing and Carnegie Hall"),
        Artist("CeeLo Green", 1974, "neo-soul", "Gnarls Barkley and Forget You"),
    ],
    (5, 31): [
        Artist("Walt Whitman", 1819, "American Transcendentalism", "Leaves of Grass and democratic vistas"),
        Artist("Clint Eastwood", 1930, "Western and beyond", "Dirty Harry and director evolution"),
        Artist("Brooke Shields", 1965, "child star model", "Blue Lagoon and Calvin Klein"),
    ],

    # June
    (6, 1): [
        Artist("Marilyn Monroe", 1926, "1950s Hollywood glamour", "pop icon blonde bombshell imagery"),
        Artist("Morgan Freeman", 1937, "authoritative voice", "Shawshank narration and dignity"),
        Artist("Heidi Klum", 1973, "supermodel mogul", "Project Runway and German glamour"),
    ],
    (6, 2): [
        Artist("Thomas Hardy", 1840, "Victorian pastoral", "Wessex countryside and rural tragedy"),
        Artist("Marquis de Sade", 1740, "libertine literature", "scandalous and provocative imagery"),
        Artist("Wayne Brady", 1972, "improv comedy", "Whose Line and musical talent"),
    ],
    (6, 3): [
        Artist("Allen Ginsberg", 1926, "Beat poetry", "Howl and counterculture San Francisco"),
        Artist("Josephine Baker", 1906, "Jazz Age", "banana skirt and Parisian cabaret"),
        Artist("Rafael Nadal", 1986, "tennis dominance", "clay court king and athletic intensity"),
    ],
    (6, 4): [
        Artist("Angelina Jolie", 1975, "contemporary cinema", "action heroine and humanitarian"),
        Artist("George III", 1738, "Georgian era", "American Revolution and English monarchy"),
        Artist("Russell Brand", 1975, "British comedy", "flamboyant wit and recovery advocacy"),
    ],
    (6, 5): [
        Artist("Federico García Lorca", 1898, "Spanish surrealism", "Andalusian duende and flamenco"),
        Artist("John Maynard Keynes", 1883, "economic theory", "Keynesian economics visualization"),
        Artist("Mark Wahlberg", 1971, "Boston tough guy", "Boogie Nights to action star"),
    ],
    (6, 6): [
        Artist("Diego Velázquez", 1599, "Spanish Golden Age", "Las Meninas and royal court realism"),
        Artist("Thomas Mann", 1875, "German literature", "Death in Venice and intellectual prose"),
        Artist("Sandra Bernhard", 1955, "alternative comedy", "one-woman show and provocative wit"),
    ],
    (6, 7): [
        Artist("Paul Gauguin", 1848, "Post-Impressionism", "Tahitian tropical paradise and bold color"),
        Artist("Prince", 1958, "musical genius", "Purple Rain and Minneapolis Sound"),
        Artist("Liam Neeson", 1952, "action transformation", "Taken and Irish gravitas"),
    ],
    (6, 8): [
        Artist("Frank Lloyd Wright", 1867, "organic architecture", "Fallingwater and Prairie Style"),
        Artist("Barbara Bush", 1925, "first lady", "white hair and family values"),
        Artist("Kanye West", 1977, "hip-hop producer", "College Dropout and fashion"),
    ],
    (6, 9): [
        Artist("Cole Porter", 1891, "Broadway sophistication", "elegant musical theater and wit"),
        Artist("Les Paul", 1915, "guitar innovation", "electric guitar and multi-track recording"),
        Artist("Michael J. Fox", 1961, "1980s icon", "Back to the Future and Parkinson's advocacy"),
    ],
    (6, 10): [
        Artist("Gustave Courbet", 1819, "French Realism", "unflinching working class scenes"),
        Artist("Maurice Sendak", 1928, "children's illustration", "Where the Wild Things Are"),
        Artist("Elizabeth Hurley", 1965, "British glamour", "safety pin dress and model elegance"),
    ],
    (6, 11): [
        Artist("Jacques Cousteau", 1910, "underwater exploration", "ocean depths and marine life"),
        Artist("Richard Strauss", 1864, "German late Romanticism", "Also Sprach Zarathustra grandeur"),
        Artist("Shia LaBeouf", 1986, "method intensity", "Transformers to art house"),
    ],
    (6, 12): [
        Artist("Anne Frank", 1929, "Holocaust remembrance", "diary and hope in darkness"),
        Artist("George H.W. Bush", 1924, "American politics", "WWII pilot and Desert Storm"),
        Artist("Adriana Lima", 1981, "supermodel", "Victoria's Secret and Brazilian beauty"),
    ],
    (6, 13): [
        Artist("William Butler Yeats", 1865, "Celtic Revival", "Irish mythology and mystical poetry"),
        Artist("Tim Allen", 1953, "sitcom dad", "Home Improvement and Toy Story voice"),
        Artist("Mary-Kate Olsen", 1986, "child star fashion", "Full House to fashion empire"),
    ],
    (6, 14): [
        Artist("Harriet Beecher Stowe", 1811, "abolitionist literature", "Uncle Tom's Cabin social impact"),
        Artist("Che Guevara", 1928, "revolutionary icon", "iconic beret portrait"),
        Artist("Boy George", 1961, "1980s androgyny", "Culture Club and gender-bending"),
    ],
    (6, 15): [
        Artist("Edvard Grieg", 1843, "Norwegian Romanticism", "Peer Gynt and Nordic landscapes"),
        Artist("Erroll Garner", 1921, "jazz piano", "Misty and self-taught brilliance"),
        Artist("Neil Patrick Harris", 1973, "versatile performer", "Doogie to Broadway"),
    ],
    (6, 16): [
        Artist("Stan Laurel", 1890, "slapstick comedy", "Laurel and Hardy silent film humor"),
        Artist("Tupac Shakur", 1971, "hip-hop poetry", "West Coast rap and social consciousness"),
        Artist("Geronimo", 1829, "Apache resistance", "Native American warrior leader"),
    ],
    (6, 17): [
        Artist("M.C. Escher", 1898, "impossible geometry", "tessellations and optical illusions"),
        Artist("Igor Stravinsky", 1882, "modernist music", "Rite of Spring and revolutionary rhythm"),
        Artist("Venus Williams", 1980, "tennis champion", "power serve and athletic style"),
    ],
    (6, 18): [
        Artist("Paul McCartney", 1942, "British Invasion pop", "Beatles and colorful psychedelia"),
        Artist("Roger Ebert", 1942, "film criticism", "thumbs up and Chicago journalism"),
        Artist("Blake Shelton", 1976, "country music", "The Voice and Nashville charm"),
    ],
    (6, 19): [
        Artist("Blaise Pascal", 1623, "mathematical philosophy", "geometry and religious meditation"),
        Artist("Paulina Rubio", 1971, "Latin pop", "Mexican pop princess"),
        Artist("Salman Rushdie", 1947, "magical realism", "Satanic Verses and literary controversy"),
    ],
    (6, 20): [
        Artist("Lionel Richie", 1949, "soul pop", "1980s smooth R&B and ballads"),
        Artist("Errol Flynn", 1909, "swashbuckler cinema", "Adventures of Robin Hood and charm"),
        Artist("Nicole Kidman", 1967, "Australian cinema", "Oscar range and ethereal beauty"),
    ],
    (6, 21): [
        Artist("Jean-Paul Sartre", 1905, "existentialism", "French intellectual and freedom philosophy"),
        Artist("Reinhold Niebuhr", 1892, "theological ethics", "Christian realism and serenity prayer"),
        Artist("Lana Del Rey", 1985, "indie pop", "vintage melancholy and Americana"),
    ],
    (6, 22): [
        Artist("Meryl Streep", 1949, "dramatic cinema", "transformative character portrayals"),
        Artist("Billy Wilder", 1906, "Hollywood master", "Some Like It Hot and Sunset Boulevard"),
        Artist("Cyndi Lauper", 1953, "1980s pop", "Girls Just Want to Have Fun and colors"),
    ],
    (6, 23): [
        Artist("Alan Turing", 1912, "computer science", "cryptography and artificial intelligence"),
        Artist("Josephine de Beauharnais", 1763, "Napoleonic era", "Empress and French Empire"),
        Artist("Selma Blair", 1972, "indie cinema", "Cruel Intentions and MS advocacy"),
    ],
    (6, 24): [
        Artist("Henry Ward Beecher", 1813, "abolitionist oratory", "moral reform and social justice"),
        Artist("Jack Dempsey", 1895, "boxing legend", "Manassa Mauler and 1920s sports"),
        Artist("Mindy Kaling", 1979, "comedy writer", "The Office and representation"),
    ],
    (6, 25): [
        Artist("Antoni Gaudí", 1852, "Catalan Modernisme", "Sagrada Família organic architecture"),
        Artist("George Orwell", 1903, "dystopian literature", "1984 and Animal Farm"),
        Artist("Carly Simon", 1945, "singer-songwriter", "You're So Vain and 1970s folk"),
    ],
    (6, 26): [
        Artist("Pearl S. Buck", 1892, "Chinese cultural", "The Good Earth and East-West bridge"),
        Artist("Claudio Abbado", 1933, "orchestral conducting", "Berlin Philharmonic elegance"),
        Artist("Ariana Grande", 1993, "pop vocal power", "whistle register and ponytail"),
    ],
    (6, 27): [
        Artist("Helen Keller", 1880, "overcoming adversity", "disability advocacy and achievement"),
        Artist("Emma Goldman", 1869, "anarchist activism", "revolutionary politics and feminism"),
        Artist("Tobey Maguire", 1975, "sensitive cinema", "Spider-Man and indie drama"),
    ],
    (6, 28): [
        Artist("Peter Paul Rubens", 1577, "Flemish Baroque", "voluptuous figures and dynamic energy"),
        Artist("Richard Rodgers", 1902, "Broadway composer", "Sound of Music and Oklahoma"),
        Artist("Elon Musk", 1971, "tech visionary", "Tesla and SpaceX futurism"),
    ],
    (6, 29): [
        Artist("Antoine de Saint-Exupéry", 1900, "aviation and fantasy", "Little Prince whimsical illustration"),
        Artist("William James Mayo", 1861, "medical innovation", "Mayo Clinic and surgery"),
        Artist("Nicole Scherzinger", 1978, "pop performer", "Pussycat Dolls and talent judging"),
    ],
    (6, 30): [
        Artist("Lena Horne", 1917, "jazz and civil rights", "glamorous African American entertainment"),
        Artist("Stanley Spencer", 1891, "British modern art", "religious scenes in English villages"),
        Artist("Mike Tyson", 1966, "boxing intensity", "heavyweight champion and controversy"),
    ],

    # July
    (7, 1): [
        Artist("Diana Spencer", 1961, "royal fashion", "Princess Diana elegance and compassion"),
        Artist("George Sand", 1804, "French Romanticism", "feminist literature and Chopin"),
        Artist("Missy Elliott", 1971, "hip-hop innovation", "Work It and visionary videos"),
    ],
    (7, 2): [
        Artist("Hermann Hesse", 1877, "spiritual journey", "Siddhartha and Eastern mysticism"),
        Artist("Thurgood Marshall", 1908, "civil rights law", "Supreme Court first and equality"),
        Artist("Lindsay Lohan", 1986, "child star drama", "Mean Girls and tabloid saga"),
    ],
    (7, 3): [
        Artist("Franz Kafka", 1883, "surrealist nightmare", "Metamorphosis and bureaucratic dread"),
        Artist("Tom Cruise", 1962, "blockbuster star", "Mission Impossible and intensity"),
        Artist("Tom Stoppard", 1937, "British theater", "Rosencrantz and Guildenstern wit"),
    ],
    (7, 4): [
        Artist("Nathaniel Hawthorne", 1804, "American Gothic", "Scarlet Letter and Puritan darkness"),
        Artist("Calvin Coolidge", 1872, "1920s America", "Silent Cal and Roaring Twenties"),
        Artist("Neil Simon", 1927, "Broadway comedy", "Odd Couple and witty dialogue"),
    ],
    (7, 5): [
        Artist("Jean Cocteau", 1889, "French avant-garde", "surrealist film and poetry"),
        Artist("P.T. Barnum", 1810, "circus spectacle", "Greatest Show on Earth and humbug"),
        Artist("Huey Lewis", 1950, "1980s rock", "Back to the Future and News"),
    ],
    (7, 6): [
        Artist("Frida Kahlo", 1907, "Mexican surrealism", "self-portraits with folk symbolism"),
        Artist("Dalai Lama", 1935, "Tibetan Buddhism", "compassion and spiritual leadership"),
        Artist("Sylvester Stallone", 1946, "action cinema", "Rocky and Rambo underdog"),
    ],
    (7, 7): [
        Artist("Marc Chagall", 1887, "dreamlike modernism", "floating lovers and Jewish folklore"),
        Artist("Gustav Mahler", 1860, "late Romantic symphony", "emotional depth and nature"),
        Artist("Ringo Starr", 1940, "Beatles rhythm", "peace and love drumming"),
    ],
    (7, 8): [
        Artist("Käthe Kollwitz", 1867, "German Expressionism", "powerful social protest and grief"),
        Artist("Nelson Rockefeller", 1908, "American politics", "New York governor and philanthropy"),
        Artist("Sophia Bush", 1982, "television drama", "One Tree Hill and activism"),
    ],
    (7, 9): [
        Artist("Tom Hanks", 1956, "American everyman", "beloved film characters and warmth"),
        Artist("Ottorino Respighi", 1879, "Italian orchestral", "Pines of Rome and tone poems"),
        Artist("Courtney Love", 1964, "grunge rock", "Hole and punk authenticity"),
    ],
    (7, 10): [
        Artist("Camille Pissarro", 1830, "Impressionism", "rural landscapes and Paris streets"),
        Artist("James Whistler", 1834, "aesthetic movement", "Mother arrangement and tone"),
        Artist("Sofia Vergara", 1972, "comedy television", "Modern Family and Colombian glamour"),
    ],
    (7, 11): [
        Artist("E.B. White", 1899, "children's literature", "Charlotte's Web and Stuart Little"),
        Artist("John Quincy Adams", 1767, "early America", "founding father's son and diplomacy"),
        Artist("Tab Hunter", 1931, "1950s heartthrob", "teen idol and Hollywood closet"),
    ],
    (7, 12): [
        Artist("Pablo Neruda", 1904, "Latin American poetry", "passionate love poems and nature"),
        Artist("Henry David Thoreau", 1817, "Transcendentalism", "Walden and civil disobedience"),
        Artist("Michelle Rodriguez", 1978, "action cinema", "Fast and Furious tough girl"),
    ],
    (7, 13): [
        Artist("Julius Caesar", 100, "Roman Imperial", "ancient Rome and classical power"),
        Artist("Harrison Ford", 1942, "blockbuster icon", "Indiana Jones and Han Solo"),
        Artist("Patrick Stewart", 1940, "Shakespearean cinema", "Picard and gravitas"),
    ],
    (7, 14): [
        Artist("Gustav Klimt", 1862, "Vienna Secession", "The Kiss and golden Byzantine style"),
        Artist("Ingmar Bergman", 1918, "Swedish cinema", "Seventh Seal and existential drama"),
        Artist("Gerald Ford", 1913, "American politics", "healing president and stumbles"),
    ],
    (7, 15): [
        Artist("Rembrandt", 1606, "Dutch Golden Age", "dramatic chiaroscuro and self-portraits"),
        Artist("Iris Murdoch", 1919, "philosophical fiction", "British intellectual novels"),
        Artist("Forest Whitaker", 1961, "transformative acting", "Last King of Scotland and soul"),
    ],
    (7, 16): [
        Artist("Corot", 1796, "Barbizon school", "soft pastoral landscapes and silvery light"),
        Artist("Barbara Stanwyck", 1907, "film noir dame", "Double Indemnity and tough independence"),
        Artist("Will Ferrell", 1967, "comedy improvisation", "SNL and Anchorman absurdity"),
    ],
    (7, 17): [
        Artist("James Cagney", 1899, "gangster film", "1930s Warner Bros crime drama"),
        Artist("Phyllis Diller", 1917, "stand-up comedy", "wild hair and self-deprecation"),
        Artist("Angela Merkel", 1954, "political leadership", "German Chancellor and pragmatism"),
    ],
    (7, 18): [
        Artist("Nelson Mandela", 1918, "liberation iconography", "anti-apartheid struggle and hope"),
        Artist("Hunter S. Thompson", 1937, "gonzo journalism", "Fear and Loathing and drugs"),
        Artist("Vin Diesel", 1967, "action franchise", "Fast and Furious family"),
    ],
    (7, 19): [
        Artist("Edgar Degas", 1834, "Impressionist", "ballet dancers and modern Paris life"),
        Artist("A.J. Cronin", 1896, "medical drama", "The Citadel and social conscience"),
        Artist("Benedict Cumberbatch", 1976, "British cinema", "Sherlock and transformation"),
    ],
    (7, 20): [
        Artist("Carlos Santana", 1947, "Latin rock", "psychedelic guitar and world fusion"),
        Artist("Gregor Mendel", 1822, "genetics pioneer", "pea plants and heredity"),
        Artist("Gisele Bündchen", 1980, "supermodel", "Brazilian beauty and runway queen"),
    ],
    (7, 21): [
        Artist("Ernest Hemingway", 1899, "modernist literature", "sparse prose and adventure"),
        Artist("Marshall McLuhan", 1911, "media theory", "medium is the message"),
        Artist("Robin Williams", 1951, "comedy genius", "improvisation and dramatic depth"),
    ],
    (7, 22): [
        Artist("Edward Hopper", 1882, "American realism", "lonely diners and urban isolation"),
        Artist("Alexander Calder", 1898, "kinetic sculpture", "mobiles and playful balance"),
        Artist("Selena Gomez", 1992, "Disney to pop star", "Wizards and Rare vulnerability"),
    ],
    (7, 23): [
        Artist("Raymond Chandler", 1888, "hard-boiled detective", "noir Los Angeles and mystery"),
        Artist("Daniel Radcliffe", 1989, "Harry Potter", "child star to Broadway"),
        Artist("Monica Lewinsky", 1973, "public figure", "scandal survival and anti-bullying"),
    ],
    (7, 24): [
        Artist("Alexandre Dumas", 1802, "swashbuckler adventure", "Three Musketeers action romance"),
        Artist("Zelda Fitzgerald", 1900, "Jazz Age", "flapper and Southern belle"),
        Artist("Jennifer Lopez", 1969, "triple threat", "Jenny from the Block and glamour"),
    ],
    (7, 25): [
        Artist("Thomas Eakins", 1844, "American realism", "rowing scenes and anatomical study"),
        Artist("Estée Lauder", 1908, "beauty empire", "cosmetics and American glamour"),
        Artist("Matt LeBlanc", 1967, "sitcom charm", "Friends Joey and Episodes"),
    ],
    (7, 26): [
        Artist("Aldous Huxley", 1894, "dystopian", "Brave New World and visionary futures"),
        Artist("Carl Jung", 1875, "analytical psychology", "archetypes and collective unconscious"),
        Artist("Mick Jagger", 1943, "rock and roll", "Rolling Stones and strutting"),
    ],
    (7, 27): [
        Artist("Hilaire Belloc", 1870, "Edwardian satire", "cautionary tales and Catholic humanism"),
        Artist("Bobbie Gentry", 1944, "country folk", "Ode to Billie Joe and mystery"),
        Artist("Maya Rudolph", 1972, "comedy versatility", "SNL impressions and Bridesmaids"),
    ],
    (7, 28): [
        Artist("Beatrix Potter", 1866, "children's illustration", "Peter Rabbit and English countryside"),
        Artist("Marcel Duchamp", 1887, "Dada conceptual", "readymades and anti-art"),
        Artist("Lori Loughlin", 1964, "television mom", "Full House and Hallmark"),
    ],
    (7, 29): [
        Artist("Vincent van Gogh", 1890, "Post-Impressionism", "death anniversary - memorial tribute"),
        Artist("Clara Bow", 1905, "silent film It Girl", "flapper and sex appeal"),
        Artist("Wil Wheaton", 1972, "geek culture", "Star Trek and web presence"),
    ],
    (7, 30): [
        Artist("Emily Brontë", 1818, "Victorian Gothic", "Wuthering Heights wild moors"),
        Artist("Henry Moore", 1898, "modernist sculpture", "reclining figures and holes"),
        Artist("Arnold Schwarzenegger", 1947, "action icon", "Terminator and bodybuilding"),
    ],
    (7, 31): [
        Artist("J.K. Rowling", 1965, "magical fantasy", "Harry Potter wizarding world"),
        Artist("Milton Friedman", 1912, "economic theory", "free market and monetarism"),
        Artist("Wesley Snipes", 1962, "action cinema", "Blade and martial arts"),
    ],

    # August
    (8, 1): [
        Artist("Herman Melville", 1819, "maritime adventure", "Moby-Dick and oceanic obsession"),
        Artist("Yves Saint Laurent", 1936, "fashion design", "Le Smoking and Parisian elegance"),
        Artist("Jason Momoa", 1979, "action star", "Aquaman and Hawaiian presence"),
    ],
    (8, 2): [
        Artist("James Baldwin", 1924, "African American literature", "Harlem and civil rights prose"),
        Artist("Carroll O'Connor", 1924, "television satire", "All in the Family and Archie"),
        Artist("Sam Worthington", 1976, "blockbuster cinema", "Avatar and action hero"),
    ],
    (8, 3): [
        Artist("Elisha Otis", 1811, "industrial innovation", "elevator and urban architecture"),
        Artist("Tony Bennett", 1926, "jazz standards", "I Left My Heart and timeless crooning"),
        Artist("Martha Stewart", 1941, "lifestyle brand", "domestic arts and entertaining"),
    ],
    (8, 4): [
        Artist("Percy Bysshe Shelley", 1792, "English Romanticism", "radical poetry and natural sublime"),
        Artist("Louis Armstrong", 1901, "jazz pioneer", "What a Wonderful World and trumpet"),
        Artist("Barack Obama", 1961, "American politics", "first Black president and hope"),
    ],
    (8, 5): [
        Artist("Guy de Maupassant", 1850, "French naturalism", "short story realism and irony"),
        Artist("John Huston", 1906, "Hollywood director", "Maltese Falcon and adventure"),
        Artist("Loni Anderson", 1945, "1980s television", "WKRP and blonde bombshell"),
    ],
    (8, 6): [
        Artist("Andy Warhol", 1928, "Pop Art", "Campbell's soup and celebrity silk screens"),
        Artist("Alfred Lord Tennyson", 1809, "Victorian poetry", "Charge of Light Brigade and laureate"),
        Artist("Vera Farmiga", 1973, "dramatic actress", "Up in the Air and horror"),
    ],
    (8, 7): [
        Artist("Mata Hari", 1876, "exotic espionage", "WWI spy glamour and orientalism"),
        Artist("Ralph Bunche", 1904, "diplomacy", "Nobel Peace Prize and UN"),
        Artist("Charlize Theron", 1975, "transformative cinema", "Monster and action glamour"),
    ],
    (8, 8): [
        Artist("Dustin Hoffman", 1937, "New Hollywood", "Graduate and character transformation"),
        Artist("Emiliano Zapata", 1879, "Mexican Revolution", "revolutionary agrarian hero"),
        Artist("Roger Federer", 1981, "tennis elegance", "graceful champion and precision"),
    ],
    (8, 9): [
        Artist("Whitney Houston", 1963, "pop diva", "powerful vocals and 1980s glamour"),
        Artist("Gillian Anderson", 1968, "television icon", "X-Files and British drama"),
        Artist("Anna Kendrick", 1985, "musical comedy", "Pitch Perfect and acerbic wit"),
    ],
    (8, 10): [
        Artist("Henri Rousseau", 1844, "naive primitivism", "jungle fantasies and bold colors"),
        Artist("Herbert Hoover", 1874, "Depression era", "humanitarian and 31st president"),
        Artist("Antonio Banderas", 1960, "Spanish cinema", "Almodóvar to Hollywood action"),
    ],
    (8, 11): [
        Artist("Alex Haley", 1921, "African heritage", "Roots and genealogical narrative"),
        Artist("Hulk Hogan", 1953, "wrestling", "Hulkamania and 1980s entertainment"),
        Artist("Chris Hemsworth", 1983, "Marvel cinema", "Thor and Australian charm"),
    ],
    (8, 12): [
        Artist("Cecil B. DeMille", 1881, "epic cinema", "Ten Commandments and biblical spectacle"),
        Artist("Erwin Schrödinger", 1887, "quantum physics", "cat paradox and wave mechanics"),
        Artist("Cara Delevingne", 1992, "model actress", "eyebrows and fashion influence"),
    ],
    (8, 13): [
        Artist("Alfred Hitchcock", 1899, "suspense cinema", "thriller and psychological tension"),
        Artist("Fidel Castro", 1926, "Cuban Revolution", "revolutionary leader and cigar"),
        Artist("Sebastian Stan", 1982, "Marvel cinema", "Winter Soldier and indie range"),
    ],
    (8, 14): [
        Artist("Doc Holliday", 1851, "Wild West", "Tombstone and frontier legend"),
        Artist("Earvin 'Magic' Johnson", 1959, "basketball", "Showtime Lakers and smile"),
        Artist("Halle Berry", 1966, "Hollywood star", "Oscar winner and action heroine"),
    ],
    (8, 15): [
        Artist("Julia Child", 1912, "culinary arts", "French cooking and kitchen warmth"),
        Artist("Napoleon Bonaparte", 1769, "Empire", "French Emperor and military genius"),
        Artist("Ben Affleck", 1972, "Hollywood evolution", "Good Will Hunting to Batman"),
    ],
    (8, 16): [
        Artist("Charles Bukowski", 1920, "dirty realism", "gritty Los Angeles and barfly life"),
        Artist("Madonna", 1958, "pop reinvention", "Material Girl and constant evolution"),
        Artist("Steve Carell", 1962, "comedy to drama", "Office and Foxcatcher range"),
    ],
    (8, 17): [
        Artist("Mae West", 1893, "pre-Code Hollywood", "brassy glamour and double entendre"),
        Artist("Davy Crockett", 1786, "frontier legend", "King of the Wild Frontier"),
        Artist("Robert De Niro", 1943, "Method acting", "Taxi Driver and Godfather"),
    ],
    (8, 18): [
        Artist("Robert Redford", 1936, "New Hollywood", "Sundance and American golden boy"),
        Artist("Virginia Dare", 1587, "colonial America", "first English child in America"),
        Artist("Christian Slater", 1969, "1980s rebel", "Heathers and Jack Nicholson cool"),
    ],
    (8, 19): [
        Artist("Coco Chanel", 1883, "haute couture", "little black dress and modern elegance"),
        Artist("Gene Roddenberry", 1921, "science fiction", "Star Trek and optimistic future"),
        Artist("John Stamos", 1963, "television heartthrob", "Full House and Beach Boys"),
    ],
    (8, 20): [
        Artist("H.P. Lovecraft", 1890, "cosmic horror", "Cthulhu and eldritch nightmare"),
        Artist("Isaac Hayes", 1942, "soul funk", "Shaft and Hot Buttered Soul"),
        Artist("Amy Adams", 1974, "versatile cinema", "Enchanted to Arrival range"),
    ],
    (8, 21): [
        Artist("Count Basie", 1904, "swing jazz", "big band and Kansas City jump"),
        Artist("Wilt Chamberlain", 1936, "basketball legend", "100 points and dominance"),
        Artist("Usain Bolt", 1986, "athletic speed", "fastest man and lightning bolt"),
    ],
    (8, 22): [
        Artist("Claude Debussy", 1862, "Impressionist music", "Clair de Lune and atmospheric tone"),
        Artist("Ray Bradbury", 1920, "science fiction", "Fahrenheit 451 and Martian Chronicles"),
        Artist("James Corden", 1978, "British television", "Late Late Show and carpool karaoke"),
    ],
    (8, 23): [
        Artist("Gene Kelly", 1912, "musical film", "Singin' in the Rain athletic dance"),
        Artist("Kobe Bryant", 1978, "basketball legend", "Mamba mentality and Lakers"),
        Artist("River Phoenix", 1970, "young Hollywood", "Stand by Me and early brilliance"),
    ],
    (8, 24): [
        Artist("Jorge Luis Borges", 1899, "magical realism", "labyrinthine libraries and infinity"),
        Artist("Max Beerbohm", 1872, "Edwardian wit", "caricature and essay"),
        Artist("Dave Chappelle", 1973, "stand-up comedy", "social commentary and sketches"),
    ],
    (8, 25): [
        Artist("Tim Burton", 1958, "Gothic fantasy", "quirky dark whimsy and stop-motion"),
        Artist("Leonard Bernstein", 1918, "American conductor", "West Side Story and Young People's Concerts"),
        Artist("Blake Lively", 1987, "Hollywood glamour", "Gossip Girl and fashion icon"),
    ],
    (8, 26): [
        Artist("Man Ray", 1890, "Dada and Surrealism", "avant-garde photography and rayographs"),
        Artist("Guillaume Apollinaire", 1880, "French avant-garde poetry", "calligrammes and modernism"),
        Artist("Macaulay Culkin", 1980, "child star", "Home Alone and grown-up cult figure"),
    ],
    (8, 27): [
        Artist("C.S. Forester", 1899, "naval adventure", "Horatio Hornblower and sea battles"),
        Artist("Lyndon B. Johnson", 1908, "American politics", "Great Society and Vietnam"),
        Artist("Aaron Paul", 1979, "prestige television", "Breaking Bad Jesse"),
    ],
    (8, 28): [
        Artist("Johann Wolfgang von Goethe", 1749, "German Romanticism", "Faust and Sturm und Drang"),
        Artist("Leo Tolstoy", 1828, "Russian literature", "War and Peace and moral philosophy"),
        Artist("Jack Black", 1969, "comedy rock", "School of Rock and Tenacious D"),
    ],
    (8, 29): [
        Artist("Ingrid Bergman", 1915, "golden age Hollywood", "Casablanca classic romance"),
        Artist("Charlie Parker", 1920, "bebop jazz", "Bird and saxophone revolution"),
        Artist("Liam Payne", 1993, "pop music", "One Direction and solo career"),
    ],
    (8, 30): [
        Artist("Mary Shelley", 1797, "Gothic horror", "Frankenstein and Romantic science"),
        Artist("Warren Buffett", 1930, "investment", "Oracle of Omaha and value"),
        Artist("Cameron Diaz", 1972, "comedy star", "There's Something About Mary"),
    ],
    (8, 31): [
        Artist("Caligula", 12, "Roman Imperial", "ancient Rome and decadent excess"),
        Artist("Maria Montessori", 1870, "educational innovation", "child-centered learning"),
        Artist("Richard Gere", 1949, "Hollywood leading man", "Pretty Woman and Buddhism"),
    ],

    # September
    (9, 1): [
        Artist("Edgar Rice Burroughs", 1875, "pulp adventure", "Tarzan and John Carter of Mars"),
        Artist("Rocky Marciano", 1923, "boxing", "undefeated heavyweight champion"),
        Artist("Zendaya", 1996, "young Hollywood", "Euphoria and Spider-Man"),
    ],
    (9, 2): [
        Artist("Keanu Reeves", 1964, "action cinema", "Matrix cyberpunk and John Wick"),
        Artist("Jimmy Connors", 1952, "tennis", "aggressive baseline and longevity"),
        Artist("Salma Hayek", 1966, "Mexican cinema", "Frida and Hollywood crossover"),
    ],
    (9, 3): [
        Artist("Louis Sullivan", 1856, "Chicago School architecture", "form follows function skyscraper"),
        Artist("Mort Walker", 1923, "comic strips", "Beetle Bailey and military humor"),
        Artist("Charlie Sheen", 1965, "Hollywood bad boy", "Wall Street and tabloid fame"),
    ],
    (9, 4): [
        Artist("Antonin Artaud", 1896, "Theatre of Cruelty", "avant-garde performance and surrealism"),
        Artist("Richard Wright", 1908, "African American literature", "Native Son and social protest"),
        Artist("Beyoncé", 1981, "pop empress", "Formation and visual albums"),
    ],
    (9, 5): [
        Artist("Louis XIV", 1638, "French Baroque", "Versailles and Sun King opulence"),
        Artist("Jesse James", 1847, "outlaw legend", "Wild West bank robber mythology"),
        Artist("Freddie Mercury", 1946, "rock opera", "Queen and Bohemian Rhapsody"),
    ],
    (9, 6): [
        Artist("Marquis de Lafayette", 1757, "American Revolution", "liberty and Franco-American ideals"),
        Artist("Jane Addams", 1860, "social reform", "Hull House and peace activism"),
        Artist("Idris Elba", 1972, "British cinema", "Luther and Bond speculation"),
    ],
    (9, 7): [
        Artist("Grandma Moses", 1860, "American folk art", "nostalgic rural landscapes and seasons"),
        Artist("Queen Elizabeth I", 1533, "Tudor England", "Virgin Queen and Elizabethan age"),
        Artist("Evan Rachel Wood", 1987, "dramatic television", "Westworld and range"),
    ],
    (9, 8): [
        Artist("Antonín Dvořák", 1841, "Czech Romanticism", "New World Symphony and Bohemian folk"),
        Artist("Peter Sellers", 1925, "comic genius", "Pink Panther and Dr. Strangelove"),
        Artist("Pink", 1979, "pop rock", "acrobatic performances and anthems"),
    ],
    (9, 9): [
        Artist("Leo Tolstoy", 1828, "Russian literary epic", "War and Peace and moral philosophy"),
        Artist("Colonel Sanders", 1890, "Kentucky Fried", "white suit and franchise empire"),
        Artist("Adam Sandler", 1966, "comedy star", "SNL to Netflix empire"),
    ],
    (9, 10): [
        Artist("Arnold Palmer", 1929, "golf", "sports and American leisure"),
        Artist("Amy Irving", 1953, "dramatic actress", "Carrie and Spielberg films"),
        Artist("Colin Firth", 1960, "British cinema", "Pride and Prejudice and King's Speech"),
    ],
    (9, 11): [
        Artist("D.H. Lawrence", 1885, "modernist literature", "sensual prose and nature mysticism"),
        Artist("O. Henry", 1862, "short stories", "twist endings and Gift of the Magi"),
        Artist("Tyler Hoechlin", 1987, "television", "Teen Wolf and Superman"),
    ],
    (9, 12): [
        Artist("Jesse Owens", 1913, "Olympic athletics", "1936 Berlin triumph and speed"),
        Artist("Barry White", 1944, "soul music", "deep voice and love unlimited"),
        Artist("Jennifer Hudson", 1981, "vocal power", "Dreamgirls and Oscar"),
    ],
    (9, 13): [
        Artist("Roald Dahl", 1916, "dark children's fantasy", "Charlie and the Chocolate Factory magic"),
        Artist("Clara Schumann", 1819, "Romantic piano", "virtuoso and Brahms muse"),
        Artist("Niall Horan", 1993, "pop music", "One Direction and Irish charm"),
    ],
    (9, 14): [
        Artist("Ivan Pavlov", 1849, "scientific psychology", "conditioning and laboratory research"),
        Artist("Margaret Sanger", 1879, "birth control pioneer", "Planned Parenthood and women's rights"),
        Artist("Amy Winehouse", 1983, "retro soul", "Back to Black and tragic voice"),
    ],
    (9, 15): [
        Artist("Agatha Christie", 1890, "cozy mystery", "Hercule Poirot and English manor murder"),
        Artist("William Howard Taft", 1857, "American politics", "president and Chief Justice"),
        Artist("Tommy Lee Jones", 1946, "character acting", "Fugitive and No Country gravitas"),
    ],
    (9, 16): [
        Artist("B.B. King", 1925, "blues guitar", "Lucille and Delta blues soul"),
        Artist("Lauren Bacall", 1924, "film noir", "To Have and Have Not and Bogart"),
        Artist("Nick Jonas", 1992, "pop music", "Jonas Brothers and solo career"),
    ],
    (9, 17): [
        Artist("Hank Williams", 1923, "country music", "honky-tonk and lonesome highway"),
        Artist("Baz Luhrmann", 1962, "maximalist cinema", "Moulin Rouge and Elvis"),
        Artist("Jimmie Johnson", 1975, "NASCAR", "seven-time champion and speed"),
    ],
    (9, 18): [
        Artist("Greta Garbo", 1905, "silent film glamour", "Hollywood golden age mystery"),
        Artist("Samuel Johnson", 1709, "English letters", "dictionary and literary criticism"),
        Artist("Jada Pinkett Smith", 1971, "actress producer", "Girls Trip and Hollywood couple"),
    ],
    (9, 19): [
        Artist("William Golding", 1911, "allegorical novel", "Lord of the Flies and human nature"),
        Artist("Cass Elliot", 1941, "1960s folk pop", "Mamas and Papas and Dream a Little Dream"),
        Artist("Jimmy Fallon", 1974, "late night television", "Tonight Show and impressions"),
    ],
    (9, 20): [
        Artist("Sophia Loren", 1934, "Italian cinema", "Mediterranean beauty and neorealism"),
        Artist("Upton Sinclair", 1878, "muckraking", "The Jungle and social reform"),
        Artist("Jon Bernthal", 1976, "intense acting", "Punisher and Walking Dead"),
    ],
    (9, 21): [
        Artist("H.G. Wells", 1866, "science fiction", "Time Machine and War of the Worlds"),
        Artist("Stephen King", 1947, "horror fiction", "It and Shining and Maine"),
        Artist("Bill Murray", 1950, "comedy legend", "Ghostbusters and deadpan"),
    ],
    (9, 22): [
        Artist("Bilbo Baggins", 1, "fantasy", "Hobbiton and Middle-earth adventure"),
        Artist("Michael Faraday", 1791, "electromagnetic", "scientific discovery and motors"),
        Artist("Tom Felton", 1987, "Harry Potter", "Draco Malfoy and British charm"),
    ],
    (9, 23): [
        Artist("John Coltrane", 1926, "jazz saxophone", "spiritual jazz and modal improvisation"),
        Artist("Ray Charles", 1930, "soul pioneer", "Georgia on My Mind and blind genius"),
        Artist("Bruce Springsteen", 1949, "rock and roll", "Born to Run and Jersey soul"),
    ],
    (9, 24): [
        Artist("F. Scott Fitzgerald", 1896, "Jazz Age", "Great Gatsby and Roaring Twenties"),
        Artist("Jim Henson", 1936, "Muppets", "Kermit and puppetry magic"),
        Artist("Kevin Sorbo", 1958, "television action", "Hercules and mythology"),
    ],
    (9, 25): [
        Artist("Mark Rothko", 1903, "color field painting", "luminous rectangles and spiritual depth"),
        Artist("William Faulkner", 1897, "Southern Gothic", "Yoknapatawpha and stream of consciousness"),
        Artist("Will Smith", 1968, "Hollywood star", "Fresh Prince to blockbuster"),
    ],
    (9, 26): [
        Artist("George Gershwin", 1898, "American musical", "Rhapsody in Blue and jazz classical fusion"),
        Artist("T.S. Eliot", 1888, "modernist poetry", "Waste Land and Four Quartets"),
        Artist("Serena Williams", 1981, "tennis greatness", "23 Grand Slams and power"),
    ],
    (9, 27): [
        Artist("Samuel Adams", 1722, "American Revolution", "Boston Tea Party and patriot imagery"),
        Artist("Meat Loaf", 1947, "rock opera", "Bat Out of Hell and theatrical"),
        Artist("Gwyneth Paltrow", 1972, "Hollywood to lifestyle", "Shakespeare in Love and Goop"),
    ],
    (9, 28): [
        Artist("Georges Clemenceau", 1841, "WWI statecraft", "French Republic and victory"),
        Artist("Confucius", 551, "Chinese philosophy", "Analects and ethical wisdom"),
        Artist("Hilary Duff", 1987, "Disney star", "Lizzie McGuire and young Hollywood"),
    ],
    (9, 29): [
        Artist("Michelangelo Antonioni", 1912, "Italian modernist cinema", "L'Avventura alienation"),
        Artist("Jerry Lee Lewis", 1935, "rock and roll", "Great Balls of Fire and wild piano"),
        Artist("Kevin Durant", 1988, "basketball", "scoring champion and slim reaper"),
    ],
    (9, 30): [
        Artist("Truman Capote", 1924, "literary journalism", "In Cold Blood and high society"),
        Artist("Elie Wiesel", 1928, "Holocaust testimony", "Night and witness"),
        Artist("Marion Cotillard", 1975, "French cinema", "La Vie en Rose Oscar"),
    ],

    # October
    (10, 1): [
        Artist("William Boeing", 1881, "aviation industry", "airplane manufacture and flight"),
        Artist("Jimmy Carter", 1924, "American politics", "39th president and humanitarian"),
        Artist("Julie Andrews", 1935, "musical cinema", "Mary Poppins and Sound of Music"),
    ],
    (10, 2): [
        Artist("Mahatma Gandhi", 1869, "nonviolent resistance", "peace and Indian independence"),
        Artist("Groucho Marx", 1890, "comedy", "Marx Brothers and wit"),
        Artist("Sting", 1951, "rock intelligence", "Police and solo artistry"),
    ],
    (10, 3): [
        Artist("Gore Vidal", 1925, "literary provocation", "political satire and essay"),
        Artist("Thomas Wolfe", 1900, "Southern literature", "Look Homeward Angel and prose"),
        Artist("Gwen Stefani", 1969, "pop rock", "No Doubt and solo reinvention"),
    ],
    (10, 4): [
        Artist("Buster Keaton", 1895, "silent comedy", "deadpan physical humor and stunts"),
        Artist("Damon Runyon", 1880, "Broadway stories", "Guys and Dolls and New York slang"),
        Artist("Susan Sarandon", 1946, "activist actress", "Thelma and Louise and conscience"),
    ],
    (10, 5): [
        Artist("Ray Kroc", 1902, "American franchising", "McDonald's and fast food culture"),
        Artist("Denis Diderot", 1713, "Enlightenment", "Encyclopedia and philosophy"),
        Artist("Kate Winslet", 1975, "British cinema", "Titanic to prestige drama"),
    ],
    (10, 6): [
        Artist("Le Corbusier", 1887, "modernist architecture", "Villa Savoie and brutalism"),
        Artist("Thor Heyerdahl", 1914, "adventure anthropology", "Kon-Tiki and exploration"),
        Artist("Elisabeth Shue", 1963, "versatile actress", "Leaving Las Vegas and Back to the Future"),
    ],
    (10, 7): [
        Artist("Yo-Yo Ma", 1955, "classical cello", "virtuoso and musical bridge-building"),
        Artist("Desmond Tutu", 1931, "anti-apartheid", "Archbishop and reconciliation"),
        Artist("Thom Yorke", 1968, "art rock", "Radiohead and experimental"),
    ],
    (10, 8): [
        Artist("Sigourney Weaver", 1949, "science fiction cinema", "Alien and strong female hero"),
        Artist("Eddie Rickenbacker", 1890, "WWI flying ace", "Medal of Honor and racing"),
        Artist("Matt Damon", 1970, "everyman star", "Bourne and Good Will Hunting"),
    ],
    (10, 9): [
        Artist("John Lennon", 1940, "rock and peace", "Beatles psychedelia and Imagine"),
        Artist("Sean Lennon", 1975, "indie rock", "musical legacy and artistry"),
        Artist("Guillermo del Toro", 1964, "dark fantasy cinema", "Pan's Labyrinth and monsters"),
    ],
    (10, 10): [
        Artist("Giuseppe Verdi", 1813, "Italian opera", "Aida and La Traviata dramatic passion"),
        Artist("Helen Hayes", 1900, "First Lady of American Theater", "Broadway royalty"),
        Artist("David Lee Roth", 1954, "rock showman", "Van Halen and frontman"),
    ],
    (10, 11): [
        Artist("Eleanor Roosevelt", 1884, "humanitarian leadership", "First Lady and human rights"),
        Artist("Henry Heinz", 1844, "food industry", "57 varieties and ketchup"),
        Artist("Michelle Trachtenberg", 1985, "television drama", "Buffy and Gossip Girl"),
    ],
    (10, 12): [
        Artist("Luciano Pavarotti", 1935, "operatic tenor", "bel canto and Three Tenors spectacle"),
        Artist("Hugh Jackman", 1968, "versatile star", "Wolverine and Broadway"),
        Artist("Marion Jones", 1975, "Olympic athletics", "track and field speed"),
    ],
    (10, 13): [
        Artist("Margaret Thatcher", 1925, "British politics", "Iron Lady and 1980s Britain"),
        Artist("Paul Simon", 1941, "folk rock poet", "Bridge Over Troubled Water and Graceland"),
        Artist("Sacha Baron Cohen", 1971, "satirical comedy", "Borat and character immersion"),
    ],
    (10, 14): [
        Artist("E.E. Cummings", 1894, "experimental poetry", "lowercase and typographical play"),
        Artist("Dwight D. Eisenhower", 1890, "WWII and presidency", "D-Day and 1950s America"),
        Artist("Usher", 1978, "R&B", "Yeah! and smooth moves"),
    ],
    (10, 15): [
        Artist("Friedrich Nietzsche", 1844, "philosophical", "Übermensch and eternal recurrence"),
        Artist("Virgil", 70, "Roman poetry", "Aeneid and classical epic"),
        Artist("Emeril Lagasse", 1959, "celebrity chef", "BAM! and Cajun cuisine"),
    ],
    (10, 16): [
        Artist("Oscar Wilde", 1854, "Victorian wit", "Aesthetic movement and dandyism"),
        Artist("Eugene O'Neill", 1888, "American drama", "Long Day's Journey and tragedy"),
        Artist("John Mayer", 1977, "singer-songwriter", "guitar virtuosity and pop"),
    ],
    (10, 17): [
        Artist("Arthur Miller", 1915, "American drama", "Death of a Salesman tragedy"),
        Artist("Rita Hayworth", 1918, "1940s Hollywood", "Gilda and pin-up glamour"),
        Artist("Eminem", 1972, "rap poetry", "8 Mile and lyrical complexity"),
    ],
    (10, 18): [
        Artist("Martina Navratilova", 1956, "tennis champion", "athletic excellence and determination"),
        Artist("Chuck Berry", 1926, "rock and roll pioneer", "Johnny B. Goode and duck walk"),
        Artist("Zac Efron", 1987, "teen to leading man", "High School Musical evolution"),
    ],
    (10, 19): [
        Artist("John le Carré", 1931, "spy novel", "cold war espionage and moral ambiguity"),
        Artist("John Lithgow", 1945, "versatile acting", "comedy and drama range"),
        Artist("Trey Parker", 1969, "animated satire", "South Park and Book of Mormon"),
    ],
    (10, 20): [
        Artist("Arthur Rimbaud", 1854, "French Symbolism", "visionary poetry and rebellion"),
        Artist("Bela Lugosi", 1882, "horror film", "Dracula and Universal monsters"),
        Artist("Snoop Dogg", 1971, "West Coast rap", "gin and juice and laid-back flow"),
    ],
    (10, 21): [
        Artist("Alfred Nobel", 1833, "invention and peace", "dynamite and Nobel Prize idealism"),
        Artist("Dizzy Gillespie", 1917, "bebop trumpet", "bent horn and jazz innovation"),
        Artist("Kim Kardashian", 1980, "reality television", "social media and empire building"),
    ],
    (10, 22): [
        Artist("Franz Liszt", 1811, "virtuoso Romanticism", "Hungarian rhapsodies and piano drama"),
        Artist("Sarah Bernhardt", 1844, "theatrical legend", "Divine Sarah and stage"),
        Artist("Jeff Goldblum", 1952, "quirky cinema", "Jurassic Park and idiosyncratic charm"),
    ],
    (10, 23): [
        Artist("Pelé", 1940, "Brazilian football", "soccer artistry and athletic grace"),
        Artist("Johnny Carson", 1925, "late night television", "Tonight Show and Americana"),
        Artist("Ryan Reynolds", 1976, "comedy star", "Deadpool and wit"),
    ],
    (10, 24): [
        Artist("Bill Wyman", 1936, "British rock", "Rolling Stones and 1960s rebellion"),
        Artist("Moss Hart", 1904, "Broadway", "You Can't Take It With You and wit"),
        Artist("Drake", 1986, "hip-hop", "Toronto sound and emotional rap"),
    ],
    (10, 25): [
        Artist("Pablo Picasso", 1881, "Cubism", "fragmented perspectives and revolutionary form"),
        Artist("Georges Bizet", 1838, "French opera", "Carmen and passionate drama"),
        Artist("Katy Perry", 1984, "pop spectacle", "Teenage Dream and maximalist shows"),
    ],
    (10, 26): [
        Artist("Hillary Clinton", 1947, "American politics", "Democratic leadership and glass ceiling"),
        Artist("Napoleon Hill", 1883, "success literature", "Think and Grow Rich and motivation"),
        Artist("Keith Urban", 1967, "country rock", "Australian Nashville star"),
    ],
    (10, 27): [
        Artist("Sylvia Plath", 1932, "confessional poetry", "Bell Jar and psychological intensity"),
        Artist("Theodore Roosevelt", 1858, "American politics", "Rough Rider and progressive"),
        Artist("John Cleese", 1939, "British comedy", "Monty Python and Fawlty Towers"),
    ],
    (10, 28): [
        Artist("Francis Bacon", 1909, "figurative expressionism", "distorted screaming popes"),
        Artist("Evelyn Waugh", 1903, "satirical fiction", "Brideshead Revisited and wit"),
        Artist("Julia Roberts", 1967, "Hollywood star", "Pretty Woman smile"),
    ],
    (10, 29): [
        Artist("Bob Ross", 1942, "happy little trees", "peaceful landscape painting instruction"),
        Artist("Fanny Brice", 1891, "comedy and music", "Funny Girl inspiration"),
        Artist("Winona Ryder", 1971, "1990s icon", "Heathers and indie queen"),
    ],
    (10, 30): [
        Artist("Diego Maradona", 1960, "Argentine football", "Hand of God and soccer brilliance"),
        Artist("John Adams", 1735, "Founding Fathers", "second president and independence"),
        Artist("Henry Winkler", 1945, "television", "Fonz and Happy Days cool"),
    ],
    (10, 31): [
        Artist("Jan Vermeer", 1632, "Dutch Golden Age", "Girl with a Pearl Earring luminosity"),
        Artist("John Keats", 1795, "English Romanticism", "Ode to a Nightingale and beauty"),
        Artist("Vanilla Ice", 1967, "1990s rap", "Ice Ice Baby and nostalgia"),
    ],

    # November
    (11, 1): [
        Artist("Stephen Crane", 1871, "American naturalism", "Red Badge of Courage and war"),
        Artist("Gary Player", 1935, "golf", "Black Knight and international champion"),
        Artist("Penn Badgley", 1986, "television drama", "Gossip Girl and You"),
    ],
    (11, 2): [
        Artist("Marie Antoinette", 1755, "French Rococo", "Versailles excess and Revolution"),
        Artist("Burt Lancaster", 1913, "golden age Hollywood", "athletic actor and drama"),
        Artist("k.d. lang", 1961, "country crossover", "androgynous voice and torch songs"),
    ],
    (11, 3): [
        Artist("Walker Evans", 1903, "documentary photography", "Depression-era America"),
        Artist("Vincenzo Bellini", 1801, "bel canto opera", "Norma and romantic melody"),
        Artist("Gabe Newell", 1962, "video game", "Valve and Steam platform"),
    ],
    (11, 4): [
        Artist("Will Rogers", 1879, "American humor", "cowboy wisdom and vaudeville"),
        Artist("Art Carney", 1918, "television comedy", "Honeymooners and character acting"),
        Artist("Matthew McConaughey", 1969, "Southern charm", "alright alright and McConaissance"),
    ],
    (11, 5): [
        Artist("Vivien Leigh", 1913, "classic Hollywood", "Gone with the Wind Southern belle"),
        Artist("Sam Shepard", 1943, "American theater", "True West and Buried Child"),
        Artist("Tilda Swinton", 1960, "art cinema", "androgynous transformation"),
    ],
    (11, 6): [
        Artist("Adolphe Sax", 1814, "musical invention", "saxophone and brass innovation"),
        Artist("John Philip Sousa", 1854, "military march", "Stars and Stripes Forever"),
        Artist("Emma Stone", 1988, "contemporary cinema", "La La Land and comedy"),
    ],
    (11, 7): [
        Artist("Marie Curie", 1867, "scientific discovery", "radium and Nobel brilliance"),
        Artist("Albert Camus", 1913, "existentialist literature", "Stranger and absurdism"),
        Artist("Joni Mitchell", 1943, "folk rock", "Both Sides Now and painterly songs"),
    ],
    (11, 8): [
        Artist("Bram Stoker", 1847, "Gothic horror", "Dracula and Victorian vampire"),
        Artist("Margaret Mitchell", 1900, "Southern epic", "Gone with the Wind"),
        Artist("Gordon Ramsay", 1966, "celebrity chef", "Hell's Kitchen and culinary excellence"),
    ],
    (11, 9): [
        Artist("Carl Sagan", 1934, "cosmic science", "Cosmos and pale blue dot wonder"),
        Artist("Ivan Turgenev", 1818, "Russian realism", "Fathers and Sons"),
        Artist("Lou Ferrigno", 1951, "bodybuilding", "Incredible Hulk and green muscle"),
    ],
    (11, 10): [
        Artist("Martin Luther", 1483, "Protestant Reformation", "95 Theses and religious revolution"),
        Artist("Richard Burton", 1925, "Shakespearean cinema", "Welsh voice and Elizabeth Taylor"),
        Artist("Eve", 1978, "hip-hop", "Let Me Blow Ya Mind and fashion"),
    ],
    (11, 11): [
        Artist("Fyodor Dostoevsky", 1821, "Russian psychological novel", "Crime and Punishment depths"),
        Artist("Kurt Vonnegut", 1922, "satirical fiction", "Slaughterhouse-Five and humanist"),
        Artist("Leonardo DiCaprio", 1974, "Hollywood star", "Titanic to Oscar"),
    ],
    (11, 12): [
        Artist("Auguste Rodin", 1840, "modern sculpture", "The Thinker and expressive bronze"),
        Artist("Grace Kelly", 1929, "Hollywood royalty", "Rear Window to Monaco"),
        Artist("Ryan Gosling", 1980, "leading man", "Drive and La La Land"),
    ],
    (11, 13): [
        Artist("Robert Louis Stevenson", 1850, "adventure fiction", "Treasure Island and Jekyll/Hyde"),
        Artist("Whoopi Goldberg", 1955, "comedy and drama", "Ghost Oscar and EGOT"),
        Artist("Gerard Butler", 1969, "action cinema", "300 and Scottish charm"),
    ],
    (11, 14): [
        Artist("Claude Monet", 1840, "Impressionism", "water lilies and cathedral haystacks"),
        Artist("Condoleezza Rice", 1954, "American politics", "Secretary of State and pianist"),
        Artist("Josh Duhamel", 1972, "Hollywood leading man", "action and romantic comedy"),
    ],
    (11, 15): [
        Artist("Georgia O'Keeffe", 1887, "American modernism", "giant flowers and desert bones"),
        Artist("Marianne Moore", 1887, "modernist poetry", "precise verse and baseball"),
        Artist("Shailene Woodley", 1991, "young adult cinema", "Divergent and activism"),
    ],
    (11, 16): [
        Artist("W.C. Handy", 1873, "blues father", "St. Louis Blues and jazz roots"),
        Artist("Burgess Meredith", 1907, "character actor", "Rocky trainer and Penguin"),
        Artist("Pete Davidson", 1993, "stand-up comedy", "SNL and personal comedy"),
    ],
    (11, 17): [
        Artist("Martin Scorsese", 1942, "New Hollywood cinema", "Taxi Driver and mean streets"),
        Artist("Rock Hudson", 1925, "golden age Hollywood", "leading man and AIDS awareness"),
        Artist("Rachel McAdams", 1978, "versatile actress", "Mean Girls to drama"),
    ],
    (11, 18): [
        Artist("Margaret Atwood", 1939, "speculative fiction", "Handmaid's Tale and dystopia"),
        Artist("Louis Daguerre", 1787, "photography pioneer", "daguerreotype invention"),
        Artist("Owen Wilson", 1968, "comedy star", "Wedding Crashers and wow"),
    ],
    (11, 19): [
        Artist("Indira Gandhi", 1917, "Indian politics", "subcontinental leadership and saris"),
        Artist("Ted Turner", 1938, "media mogul", "CNN and Atlanta Braves"),
        Artist("Jodie Foster", 1962, "child star to director", "Taxi Driver to Oscar winner"),
    ],
    (11, 20): [
        Artist("Nadine Gordimer", 1923, "South African literature", "apartheid-era social commentary"),
        Artist("Robert F. Kennedy", 1925, "American politics", "civil rights and tragedy"),
        Artist("Bo Derek", 1956, "1980s glamour", "10 and cornrows"),
    ],
    (11, 21): [
        Artist("René Magritte", 1898, "Belgian Surrealism", "bowler hats and conceptual mystery"),
        Artist("Voltaire", 1694, "Enlightenment satire", "Candide and philosophical wit"),
        Artist("Björk", 1965, "avant-garde pop", "Icelandic experimental and swan dress"),
    ],
    (11, 22): [
        Artist("George Eliot", 1819, "Victorian realism", "Middlemarch and moral complexity"),
        Artist("Hoagy Carmichael", 1899, "American songbook", "Stardust and jazz standards"),
        Artist("Scarlett Johansson", 1984, "Hollywood star", "Black Widow and indie range"),
    ],
    (11, 23): [
        Artist("José Clemente Orozco", 1883, "Mexican muralism", "revolutionary frescoes and social justice"),
        Artist("Boris Karloff", 1887, "horror film", "Frankenstein's monster and Universal"),
        Artist("Miley Cyrus", 1992, "pop transformation", "Hannah Montana to provocateur"),
    ],
    (11, 24): [
        Artist("Henri de Toulouse-Lautrec", 1864, "Post-Impressionism", "Moulin Rouge posters and nightlife"),
        Artist("Scott Joplin", 1868, "ragtime", "Maple Leaf Rag and syncopation"),
        Artist("Katherine Heigl", 1978, "television to cinema", "Grey's Anatomy and rom-com"),
    ],
    (11, 25): [
        Artist("Andrew Carnegie", 1835, "Gilded Age philanthropy", "steel and library building"),
        Artist("Joe DiMaggio", 1914, "baseball legend", "Yankee Clipper and Marilyn"),
        Artist("Christina Applegate", 1971, "sitcom star", "Married with Children to drama"),
    ],
    (11, 26): [
        Artist("Charles Schulz", 1922, "comic strip", "Peanuts and Charlie Brown wisdom"),
        Artist("Tina Turner", 1939, "rock and soul", "What's Love Got to Do with It"),
        Artist("DJ Khaled", 1975, "hip-hop producer", "We the Best and anthem making"),
    ],
    (11, 27): [
        Artist("Bruce Lee", 1940, "martial arts cinema", "Enter the Dragon action poetry"),
        Artist("Jimi Hendrix", 1942, "rock guitar", "Purple Haze and feedback mastery"),
        Artist("Bill Nye", 1955, "science education", "Science Guy and climate advocacy"),
    ],
    (11, 28): [
        Artist("William Blake", 1757, "visionary Romanticism", "Songs of Innocence and illuminated prints"),
        Artist("Claude Lévi-Strauss", 1908, "structural anthropology", "Tristes Tropiques and myth"),
        Artist("Jon Stewart", 1962, "satirical news", "Daily Show and political comedy"),
    ],
    (11, 29): [
        Artist("Louisa May Alcott", 1832, "American domestic fiction", "Little Women and New England"),
        Artist("C.S. Lewis", 1898, "Christian fantasy", "Narnia and apologetics"),
        Artist("Don Cheadle", 1964, "dramatic actor", "Hotel Rwanda and War Machine"),
    ],
    (11, 30): [
        Artist("Mark Twain", 1835, "American satire", "Tom Sawyer and Mississippi River"),
        Artist("Jonathan Swift", 1667, "satirical literature", "Gulliver's Travels and modest proposals"),
        Artist("Ridley Scott", 1937, "visual cinema", "Blade Runner and Gladiator"),
    ],

    # December
    (12, 1): [
        Artist("Woody Allen", 1935, "New York comedy", "neurotic intellectual and jazz"),
        Artist("Rex Stout", 1886, "detective fiction", "Nero Wolfe and orchids"),
        Artist("Sarah Silverman", 1970, "provocative comedy", "taboo humor and activism"),
    ],
    (12, 2): [
        Artist("Georges Seurat", 1859, "Pointillism", "tiny dots of color and Sunday afternoon"),
        Artist("Maria Callas", 1923, "opera diva", "La Divina and dramatic soprano"),
        Artist("Britney Spears", 1981, "pop princess", "Baby One More Time and comeback"),
    ],
    (12, 3): [
        Artist("Jean-Luc Godard", 1930, "French New Wave cinema", "Breathless and jump cuts"),
        Artist("Joseph Conrad", 1857, "literary modernism", "Heart of Darkness and sea"),
        Artist("Julianne Moore", 1960, "dramatic actress", "Still Alice and range"),
    ],
    (12, 4): [
        Artist("Wassily Kandinsky", 1866, "abstract expressionism", "colorful geometric spirituality"),
        Artist("Edith Cavell", 1865, "WWI nursing", "heroic sacrifice and compassion"),
        Artist("Jay-Z", 1969, "hip-hop mogul", "Brooklyn rap and business empire"),
    ],
    (12, 5): [
        Artist("Walt Disney", 1901, "animation", "Mickey Mouse and fantastical entertainment"),
        Artist("Little Richard", 1932, "rock and roll", "Tutti Frutti and flamboyance"),
        Artist("Frankie Muniz", 1985, "child star", "Malcolm in the Middle"),
    ],
    (12, 6): [
        Artist("Ira Gershwin", 1896, "Broadway lyrics", "Porgy and Bess and American songbook"),
        Artist("Dave Brubeck", 1920, "cool jazz", "Take Five and time signatures"),
        Artist("Nick Park", 1958, "claymation", "Wallace and Gromit and Aardman"),
    ],
    (12, 7): [
        Artist("Willa Cather", 1873, "prairie literature", "My Antonia and American frontier"),
        Artist("Noam Chomsky", 1928, "linguistics and politics", "generative grammar and activism"),
        Artist("Jennifer Carpenter", 1979, "television drama", "Dexter intensity"),
    ],
    (12, 8): [
        Artist("Diego Rivera", 1886, "Mexican muralism", "Frida's husband and grand social frescoes"),
        Artist("Jean Sibelius", 1865, "Finnish nationalism", "Finlandia and Nordic romance"),
        Artist("Nicki Minaj", 1982, "rap queen", "Super Bass and alter egos"),
    ],
    (12, 9): [
        Artist("Judi Dench", 1934, "British theatre", "Shakespearean gravitas and wit"),
        Artist("John Milton", 1608, "epic poetry", "Paradise Lost and English literature"),
        Artist("Felicity Huffman", 1962, "television drama", "Desperate Housewives and range"),
    ],
    (12, 10): [
        Artist("Emily Dickinson", 1830, "American poetry", "reclusive verse and nature meditation"),
        Artist("Thomas Merton", 1915, "spiritual writing", "Seven Storey Mountain and contemplation"),
        Artist("Raven-Symoné", 1985, "Disney star", "That's So Raven and Cheetah Girls"),
    ],
    (12, 11): [
        Artist("Aleksandr Solzhenitsyn", 1918, "Russian dissident literature", "Gulag Archipelago"),
        Artist("Hector Berlioz", 1803, "French Romanticism", "Symphonie fantastique and orchestration"),
        Artist("Hailee Steinfeld", 1996, "young Hollywood", "True Grit and pop music"),
    ],
    (12, 12): [
        Artist("Edvard Munch", 1863, "Expressionism", "The Scream and psychological angst"),
        Artist("Gustave Flaubert", 1821, "French realism", "Madame Bovary and style"),
        Artist("Frank Sinatra", 1915, "American songbook", "My Way and Rat Pack cool"),
    ],
    (12, 13): [
        Artist("Taylor Swift", 1989, "pop music", "storytelling and stadium spectacle"),
        Artist("Heinrich Heine", 1797, "German Romanticism", "lyric poetry and irony"),
        Artist("Jamie Foxx", 1967, "multi-talent", "Ray Oscar and comedy"),
    ],
    (12, 14): [
        Artist("Nostradamus", 1503, "prophecy", "mysterious predictions and occult imagery"),
        Artist("Tycho Brahe", 1546, "Renaissance astronomy", "stellar observation and prosthetic nose"),
        Artist("Vanessa Hudgens", 1988, "Disney star", "High School Musical and Broadway"),
    ],
    (12, 15): [
        Artist("Gustave Eiffel", 1832, "iron architecture", "Eiffel Tower and industrial elegance"),
        Artist("J. Paul Getty", 1892, "oil magnate", "Getty Museum and wealth"),
        Artist("Don Johnson", 1949, "1980s television", "Miami Vice and pastel suits"),
    ],
    (12, 16): [
        Artist("Wassily Kandinsky", 1866, "abstract pioneer", "spiritual geometric compositions"),
        Artist("Jane Austen", 1775, "Regency romance", "Pride and Prejudice and wit"),
        Artist("Theo James", 1984, "young Hollywood", "Divergent and British charm"),
    ],
    (12, 17): [
        Artist("Ludwig van Beethoven", 1770, "Classical-Romantic transition", "Ninth Symphony and heroic struggle"),
        Artist("Erskine Caldwell", 1903, "Southern Gothic", "Tobacco Road and rural poverty"),
        Artist("Milla Jovovich", 1975, "action cinema", "Resident Evil and fashion"),
    ],
    (12, 18): [
        Artist("Paul Klee", 1879, "Bauhaus abstract", "childlike color and whimsical geometry"),
        Artist("Steven Spielberg", 1946, "blockbuster cinema", "E.T. and Schindler's List"),
        Artist("Brad Pitt", 1963, "Hollywood star", "Fight Club to producer"),
    ],
    (12, 19): [
        Artist("Édith Piaf", 1915, "French chanson", "La Vie en Rose and Parisian heartbreak"),
        Artist("Leonid Brezhnev", 1906, "Soviet era", "Cold War stagnation and eyebrows"),
        Artist("Alyssa Milano", 1972, "television actress", "Who's the Boss and activism"),
    ],
    (12, 20): [
        Artist("Uri Geller", 1946, "paranormal", "spoon bending and psychic phenomena"),
        Artist("Harvey Firestone", 1868, "tire industry", "rubber and automotive"),
        Artist("Jonah Hill", 1983, "comedy to drama", "Superbad to Oscar noms"),
    ],
    (12, 21): [
        Artist("Frank Zappa", 1940, "avant-garde rock", "experimental satire and Mothers of Invention"),
        Artist("Benjamin Disraeli", 1804, "Victorian politics", "Prime Minister and novels"),
        Artist("Samuel L. Jackson", 1948, "cinema icon", "Pulp Fiction and versatility"),
    ],
    (12, 22): [
        Artist("Jean-Michel Basquiat", 1960, "neo-expressionism", "graffiti crowns and raw street art"),
        Artist("Giacomo Puccini", 1858, "Italian opera", "La Bohème and Madama Butterfly"),
        Artist("Ralph Fiennes", 1962, "British cinema", "Schindler's List and Voldemort"),
    ],
    (12, 23): [
        Artist("Emperor Akihito", 1933, "Japanese Imperial", "modern Japanese dignity and tradition"),
        Artist("Madame C.J. Walker", 1867, "entrepreneurship", "first female self-made millionaire"),
        Artist("Eddie Vedder", 1964, "grunge rock", "Pearl Jam and raw vocals"),
    ],
    (12, 24): [
        Artist("Howard Hughes", 1905, "aviation and Hollywood", "eccentric billionaire and Spruce Goose"),
        Artist("Ricky Martin", 1971, "Latin pop", "Livin' La Vida Loca and crossover"),
        Artist("Ryan Seacrest", 1974, "television host", "American Idol and New Year's"),
    ],
    (12, 25): [
        Artist("Humphrey Bogart", 1899, "film noir", "Casablanca and hard-boiled detective"),
        Artist("Isaac Newton", 1642, "scientific revolution", "gravity and calculus"),
        Artist("Sissy Spacek", 1949, "dramatic actress", "Carrie and Coal Miner's Daughter"),
    ],
    (12, 26): [
        Artist("Henry Miller", 1891, "transgressive literature", "Tropic of Cancer and bohemian Paris"),
        Artist("Mao Zedong", 1893, "Chinese Revolution", "communist leader and Cultural Revolution"),
        Artist("Jared Leto", 1971, "method actor musician", "Dallas Buyers Club and 30 Seconds to Mars"),
    ],
    (12, 27): [
        Artist("Johannes Kepler", 1571, "astronomical", "planetary motion and cosmic harmony"),
        Artist("Louis Pasteur", 1822, "microbiology", "pasteurization and germ theory"),
        Artist("Timothée Chalamet", 1995, "young Hollywood", "Call Me By Your Name and Dune"),
    ],
    (12, 28): [
        Artist("Denzel Washington", 1954, "dramatic cinema", "powerful performances and integrity"),
        Artist("Woodrow Wilson", 1856, "American politics", "WWI president and League of Nations"),
        Artist("John Legend", 1978, "soul music", "All of Me and EGOT"),
    ],
    (12, 29): [
        Artist("Pablo Casals", 1876, "classical cello", "virtuoso and Catalan peace advocate"),
        Artist("Mary Tyler Moore", 1936, "television pioneer", "MTM and sitcom revolution"),
        Artist("Jude Law", 1972, "British cinema", "Talented Mr. Ripley and versatility"),
    ],
    (12, 30): [
        Artist("Rudyard Kipling", 1865, "British colonial literature", "Jungle Book and Just So Stories"),
        Artist("Patti Smith", 1946, "punk poetry", "Horses and rock rebellion"),
        Artist("LeBron James", 1984, "basketball greatness", "King James and legacy"),
    ],
    (12, 31): [
        Artist("Henri Matisse", 1869, "Fauvism", "bold color cutouts and joyful expression"),
        Artist("John Denver", 1943, "folk pop", "Rocky Mountain High and sunshine"),
        Artist("Anthony Hopkins", 1937, "transformative acting", "Hannibal Lecter and range"),
    ],
}


def get_artist_of_the_day(today: date | None = None) -> Artist | None:
    """Get an artist for today's date with rotation based on hour."""
    if today is None:
        today = date.today()

    key = (today.month, today.day)
    artists = ARTISTS_BY_DATE.get(key)

    if not artists:
        return None

    if len(artists) == 1:
        return artists[0]

    # Rotate based on hour of day
    hour = datetime.now().hour
    # Divide 24 hours by number of artists
    hours_per_artist = 24 // len(artists)
    index = min(hour // hours_per_artist, len(artists) - 1)

    return artists[index]


def get_all_artists_for_date(today: date | None = None) -> list[Artist]:
    """Get all artists for a given date."""
    if today is None:
        today = date.today()

    key = (today.month, today.day)
    return ARTISTS_BY_DATE.get(key, [])


def get_artist_style_prompt(artist: Artist) -> str:
    """Generate a style prompt based on the artist."""
    return f"in the style of {artist.name}, featuring {artist.description}"
