from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi



# import CRUD operations for Lesson1
from database_setup import Base,Restaurant,MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



#create session and connect to DB
engine = create_engine('sqlite:///restaurant.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()






## Handler code indicates what code to execute  based on type of http request that is sent to the server

class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            #Objective 3 step2 - create/restaurants/newpage
            if self.path.endswith("/restaurants/new"):
               self.send_response(200)
               self.send_header('Content-type', ' text-html')
               self.end_headers()
               output = ""
               output += "<html><body>"
               output += "<h1>Make a new restaurant</h1>"
               output += "<form method = 'POST' enctype = 'multipart/form-data' action = '/restaurants/new'>"
               output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name'>"
               output += "<input type = 'submit' value ='Create'>"
               output += "</form><body</html>"
               self.wfile.write(output)
               print output
               return
            
                # creates edit page
            if self.path.endswith("/edit"):
                # to get the ID spilt command is used returns array of string seperated by slash
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text-html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>"
                    output += myRestaurantQuery.name
                    output += "</h1>"
                    
                    output += "<form method='POST' enctype = 'multipart/form-data' action = '/restaurants/%s/edit'>"% restaurantIDPath
                    output +="<input name = 'newRestaurantName' type='text' placeholder = '%s'>" % myRestaurantQuery.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
        
                # creates delete page
            if self.path.endswith("/delete"):
               restaurantIDPath = self.path.split("/")[2]
               myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
               if myRestaurantQuery:
                   self.send_response(200)
                   self.send_header('Content-type', 'text-html')
                   self.end_headers()
                   output  = ""
                   output +="<html><body"
                   output += "<h1>Are you sure you want to delete %s?" % myRestaurantQuery.name
                   output += "<form method='POST' enctype='multipart/form-data' action = '/restaurants/%s/delete'>"% restaurantIDPath
                   output += "<input name = 'newRestaurantName' type='text' placeholder = '%s'>" % myRestaurantQuery.name
                   output += "<input type = 'submit' value = 'Delete'>"
                   output += "<body><html>"
                   self.wfile.write(output)

            # objective 1
            if self.path.endswith("/restaurants"):
              restaurants = session.query(Restaurant).all()
              self.send_response(200)
              self.send_header('Content-type', 'text/html')
              self.end_headers()
              output = ""
              output += "<a href = '/restaurants/new'>Make a new Restaurant here</a><br><br>"
              output += "<html><body>"

              for restaurant in restaurants:
                  output += restaurant.name
                  output += "</br>"
                  # Add Edit and Delete links# Replace edit href
                  output += "<a href = 'restaurants/%s/edit'>Edit</a>" % restaurant.id
                  output += "</br>"
                  # Replace Delete href
                  output += "<a href = ' restaurants/%s/delete '>Delete</a>" % restaurant.id
                  output += "</br></br></br>"
              output += "<body><html>"
              self.wfile.write(output)
              return




            if self.path.endswith("/hello"):
              self.send_response(200)
              self.send_header('Content-type', 'text/html')
              self.end_headers()
              output = ""
              output += "<html><body>"
              output += "<h1>Hello!</h1>"
              output += "<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>what would you like me to say?</h2><input name = 'message' type='text'<input type='submit' value='Submit'> </form>"
              output += "</body></html>"
              self.wfile.write(output)
              print output
              return

            if self.path.endswith("/hola"):
               self.send_response(200)
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               output = ""
               output += "<html><body>"
               output += "<h1>#161 Hola! <a href = 'hello'>Back to Hello</body></html></h1>"
               output += "<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>what would you like me to say?</h2><input name = 'message' type='text'<input type='submit' value='Submit'> </form>"
               self.wfile.write(output)
               print output
               return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
           if self.path.endswith("/edit"):
               ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
               if ctype == 'multipart/form-data':
                   fields = cgi.parse_multipart(self.rfile, pdict)
                   messagecontent = fields.get('newRestaurantName')
                   restaurantIDPath = self.path.split("/")[2]

                   myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()

                   if myRestaurantQuery != []:
                       myRestaurantQuery.name = messagecontent[0]
                       session.add(myRestaurantQuery)
                       session.commit()
                       self.send_response(301)
                       self.send_header('content-type', 'text/html')
                       self.send_header('Location', '/restaurants')
                       self.end_headers()

           if self.path.endswith("/delete"):
               restaurantIDPath = self.path.split("/")[2]
               myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
           
               if myRestaurantQuery:
                   session.delete(myRestaurantQuery)
                   session.commit()
                   self.send_response(301)
                   self.send_header('Content-type', 'text/html')
                   self.send_header('Location', '/restaurants')
                   self.end_headers()
    

           if self.path.endswith("/restaurants/new"):
             ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
             if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile,pdict)
                messagecontent = fields.get('newRestaurantName')
 

                # create new Restaurant object
                newRestaurant = Restaurant(name=messagecontent[0])
                session.add(newRestaurant)
                session.commit()


           self.send_response(301)
           self.send_header('Content-type', 'text/html')
           self.send_header('Location', '/restaurants')
           self.end_headers()

            #self.send_response(301)
            #self.send_header('Content-type', 'text/html')
            #self.end_headers()

           #ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
           # if ctype == 'multipart/form-data':
              #fields=cgi.parse_multipart(self.rfile,pdict)
              # messagecontent = fields.get('message')

           #output = ""
           #output += "<html><body>"
           #output += "<h2>Okay, how about this </h2>"
           #output += "<h1> %s </h1>"% messagecontent[0]

           #output += "<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>what would you like me to say?</h2><input name = 'message' type='text'<input type='submit' value='Submit'> </form>"
           #output += "</body></html>"
           #self.wfile.write(output)
           #print output
           #return

        except:
            pass




## In main we will instantiate our server and specifies on what port we will listen
def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webServerHandler)
        print "Web server running on port %s" %port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
    ## Immediately run the main method when python interpreter executes the script
