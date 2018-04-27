// Get market data based on ICO.
$.get( "/get-currency?ico=rcn", function( data ) {
  console.log( data);
});

// Get complete market summaries.
$.get( "/get-summaries", function( data ) {
  console.log( data);
});