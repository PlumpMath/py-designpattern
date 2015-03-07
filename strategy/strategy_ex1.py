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
 
 class ImageFinder:
    ''' Inteface / Abstract Class concept for readability.'''

    def find(self, image):
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, ImageFinder is supposed to be an interface / abstract class!')

class ImageFinderFlickr(ImageFinder):
    ''' Locates images in flickr'''

    def find(self, image):
        # in reality, query Flickr API for image path
        return "Found image in Flickr: " + image


class ImageFinderDatabase(ImageFinder):
    ''' Locates images in database. '''
    def find(self, image):
        #in reality, query database for image path
        return "Found image in database: " + image
    
    
    
if __name__ == "__main__" :

    finderBase = ImageFinder()
    finderFlickr = ImageFinderFlickr()
    finderDatabase = ImageFinderDatabase()

    try:
        #this is going to blow up!
        print finderBase.find('chickens')
    except NotImplementedError as e:
        print "The following exception was expected:"
        print e
        

    print finderFlickr.find('chickens')
    print finderFlickr.find('rabbits')
    print finderDatabase.find('dogs')
    print finderDatabase.find('cats')  