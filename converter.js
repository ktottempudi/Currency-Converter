
function convert_money(amount, initialCurrency, finalCurrency) {
	if(initialCurrency == "" || amount == "" || finalCurrency == ""){
		alert("fill in all of the fields")
	}
	else{
		if(initialCurrency != finalCurrency){
			retrieve_rate();
		}
		else{
			document.getElementById('output').value = amount;
		}
	}
}

initialCurrency = document.getElementById('inputMenu');
amount = document.getElementById('initialNum');
finalCurrency = document.getElementById('outputMenu');

document.onkeydown = function(event){
	if(event.keyCode == 13){
		if(initialCurrency.value == "" || amount.value == "" || finalCurrency.value == ""){
			alert("fill in all of the fields")
		}
		else{
			if(initialCurrency.value != finalCurrency.value){
				retrieve_rate();
			}
			else{
				document.getElementById('output').value = amount.value;
			}
		}
	}
}

function retrieve_rate(){
			let url = new URL("http://localhost:8000");
			let params = {fcurrency:initialCurrency.value, scurrency:finalCurrency.value}
			url.search = new URLSearchParams(params).toString();
			fetch(url, {mode: 'cors'})
				.then(response => response.text())
				.then(data => {
					converted_amount = amount.value * parseFloat(data);
					document.getElementById('output').value = converted_amount;
				})
				.catch(error => console.log(error))
}
