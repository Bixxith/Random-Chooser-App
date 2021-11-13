<h1> Chooser App </h1>

Chooser App is a web application made using Python and Flask. <br>
The purpose of this app is to aid in the decision making process for some common non-important choices.<br>
It uses basic apis to pull lists of items based on a few inputs and then returns one at random.<br>


<h4>Possible Decisions to Be Made:</h4>
<ul>
<li>Where should I eat lunch today?</li>
<li>What movie should I watch tonight?</li>
<li>What video game should I play tonight?</li>
</ul>


<h2> Restaurant Chooser App </h2>

The Restaurant Chooser App takes three points of data to return a random location to eat at.  It uses Google's geocoding API, places API, and map embed API.
<h4>Input Fields</h4>
<ul>
<li>Location: This is a required input field to begin the search.  It accepts street addresses, cities, and zip codes.</li>
<li>Search Term: This is an optional input field.  If let empty it will return any restaurants that are within the given radius. 
Due to limitations with the API the search term may not yield perfect results.  For instance, searching for pizza in my local area sometimes includes Subway and Burger King in the results.  </li>
<li>Mile Radius: This is a required input field as it determines how far to look for a restaurant. It will not look over 100 miles from the point of origin and will not look under 0 miles. </li>
</ul>
<br>
After submitting the required inputs the app will return the name of the restaurant and display an embedded google map with location information.

<h2> Movie Chooser App </h2>
<p>TBI</P>
<h2> TV Show Chooser App </h2>
<p>TBI</P>
<h2> Video Game Chooser App </h2>
<p>TBI</P>
<h2> Book Chooser App </h2>
<p>TBI</P>
