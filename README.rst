HOW TO INSTALL
--------------
To install run ``pip install kyu_ar_kowd_jenereytor`` or ``easy_install kyu_ar_kowd_jenereytor``.


SAMPLE CODE
------------
::

	from kyu_ar_kowd_jenereytor import Jenereytor, JenereytorInvalidHeightException, JenereytorInvalidTextException, JenereytorInvalidWidthException

	if __name__ == "__main__":
	    
	    qrCodeGenerator = Jenereytor()
	    
	    try:
		pngFile = '/home/six519/Desktop/qrcode.png'
		if qrCodeGenerator.generate('Hello World', pngFile):
		    print "Image saved to %s" % pngFile
		else:
		    print "Cannot generate QR Code"
	    except (JenereytorInvalidHeightException, JenereytorInvalidTextException, JenereytorInvalidWidthException) as e :
		print "An error occurred: %s" % e
