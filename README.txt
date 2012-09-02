Every Month: 
get new cassini images after they are posted to pds-rings.seti.org/saturn/cassini
by running these scripts in the following order:

1.  parser.py      get all the images and put them into the database - or use admin by hand
2.  get_media.py   get the image files, tweek the filter to get only pub_order = null, new ones!
3.  shuffle.py     shuffle the new images into the collection (pub orders)

copy the new database and media files up to server

Annually:
the best way to continue is to null out the dates in 1/3 of the rows ordered by oldest
pub_date first. This lets people still use the back button to see previous posts
