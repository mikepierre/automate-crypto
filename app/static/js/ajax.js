function getCoinData(){
	$.get( "/get-currency?ico=rcn", function( data ) {
	  console.log( data);
	  console.log(data[0].Ask);
	});
}

// Get complete market summaries.
/*
$.get( "/get-summaries", function( data ) {
  console.log( data);
});
*/