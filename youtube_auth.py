client_id = "4092757862.apps.googleusercontent.com"

url = "https://accounts.google.com/o/oauth2/auth?" +
  	"client_id=" client_id + "&" +
  	+ "redirect_uri=http://localhost/oauth2callback&" +
  	"scope=https://www.googleapis.com/auth/youtube&" +
  	"response_type=code&" +
  	"access_type=offline"