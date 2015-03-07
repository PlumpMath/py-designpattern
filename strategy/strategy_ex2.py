/**
 * Copyright 2011 Laurence Gellert
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *     http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

class ImageFinder(object):
    """
	In this example the base object ImageFinder keeps a copy
    of the concrete class (strategy).  You may also set
    a default strategy to use which might be convienient.
    In this case it is set to None which forces the caller
    to supply a concrete class.
        
    The concrete find method is supplied with an instance of
    this object so its state can be tracked.
    """
    
    def __init__(self, strategy=None):
        self.action = None
        self.count = 0
        if strategy:
            #get a handle to the object
            self.action = strategy()
    
    def find(self, image):
        if(self.action):
            self.count += 1
            return self.action.find(image, self)
        else: 
            raise UnboundLocalError('Exception raised, no strategyClass supplied to ImageFinder!')

class ImageFinderFlickr(object):
    ''' Locates images in Flickr. '''

    def find(self, image, instance):
        # in reality, query Flickr API for image path
        return "Found image in Flickr: " + image + ", search #" + str(instance.count)


class ImageFinderDatabase(object):
    ''' Locates images in database. '''
    def find(self, image, instance):
        #in reality, query database for image path
        return "Found image in database: " + image + ", search #" + str(instance.count)
    
    
if __name__ == "__main__" :

    finderBase = ImageFinder()
    #these next two look a little convuluted don't they?
    #useage is a little more verbose in example 2 vs example 1
    #however, benefits in include a default strategy type, and ability to track state
    finderFlickr = ImageFinder(strategy=ImageFinderFlickr)
    finderDatabase = ImageFinder(strategy=ImageFinderDatabase)

    try:
        #this is going to blow up!
        print finderBase.find('chickens')
    except Exception as e:
        print "The following exception was expected:"
        print e
        

    print finderFlickr.find('chickens')
    print finderFlickr.find('bugs bunny')
    print finderFlickr.find('tweety')
    print finderDatabase.find('dogs')
    print finderDatabase.find('cats')
    print finderDatabase.find('rabbits')