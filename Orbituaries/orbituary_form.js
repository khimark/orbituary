// script.js

const form = document.getElementById('obituary_form');

form.addEventListener('submit', (e) => {
	e.preventDefault();
	
	const name = document.getElementById('name').value;
	const dob = document.getElementById('dob').value;
	const dod = document.getElementById('dod').value;
	const content = document.getElementById('content').value;
	const author = document.getElementById('author').value;
	
	if (name === '' || dob === '' || dod === '' || content === '' || author === '') {
		alert('Please fill in all fields');
		return;
	}
	
	// Add additional validation logic here if needed
	
	form.submit();
});