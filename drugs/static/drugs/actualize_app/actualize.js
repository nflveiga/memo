$( document ).ready(function() {
    
  $('#up2dtr-form').submit(function(event){
      event.preventDefault();
      var q=$('#query').val()
      q=q.split(' ').join('+');
      var search_link="http://www.uptodate.com.sci-hub.bz/contents/search?search="+q+"&x=0&y=0"
      window.open(search_link)
})  
    
    
})