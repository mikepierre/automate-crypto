function getCoinData() {
	$.get( "/get-currency?ico=rcn", function( data ) {
	  $( document ).ready(function() {
		  $("#ask").text(data.result[0].Ask);
		  $("#baseVolume").text(data.result[0].BaseVolume);
		  $("#bid").text(data.result[0].Bid);
		  $("#created").text(data.result[0].Created);
		  $("#high").text(data.result[0].High);
		  $("#last").text(data.result[0].Last);
		  $("#low").text(data.result[0].Low);
		  $("#marketName").text(data.result[0].MarketName);
		  $("#openBuyOrders").text(data.result[0].OpenBuyOrders);
		  $("#openSellOrders").text(data.result[0].OpenSellOrders);
		  $("#prevDate").text(data.result[0].PrevDay);
		  $("#timeStamp").text(data.result[0].TimeStamp);
		  $("#volume").text(data.result[0].Volume);
	  });
	});
}

// Get complete market summaries.
/*
$.get( "/get-summaries", function( data ) {
  console.log( data);
});
*/
