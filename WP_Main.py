import WP_Lib as GM

GM.BOMB("url.txt")
print GM.successUrl
#GM.FIRE("http://hr.tufts.edu")			#A Bug Lies Here: *requests.get does NOT return at all, no matter the timeout argument, p.s Chrome says "Err Connection Reset"
#GM.FIRE("iseri.es/")					#Sample Wordpress Site
#GM.FIRE("http://www.kaiseigakuen.jp")				#Another Weird site...
#GM.FIRE("http://www.criticalresistance.org")

