for year in 1896 1900 1904 1906 1908 1912 1920 1924 1928 1932 1936 1948 1952 1956 1960 1964 1968 1972 1976 1980 1984 1988 1992 1996 2000 2004 2008 2012 2016; do
  wget https://en.wikipedia.org/wiki/Athletics_at_the_${year}_Summer_Olympics -O html/$year.html
done
