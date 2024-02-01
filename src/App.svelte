<script>
	//import App from './App.svelte'; 
	let name = 'Harini';
	let beltColour = 'Blue';
</script>

<main>
	<h1>Hello {name}!</h1>
	<p> {beltColour} belt</p>
</main>

<div id="app">
	<!-- Your component content here -->
  
	<h1>Hello from Your Chrome Extension</h1>
	<p>This is a simple example.</p>
  
	<!-- Add more components and content as needed -->
  
</div>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 500px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	:global(body) {
    margin: 0;
    overflow: hidden;
    height: 100%;
    width: 100%;
    }

	#app {
		width: 1000px; 
		height: 300px; 
		padding: 20px;
		background-color: white;
	}
</style>

<!-- <script>
	let message = "Hello, Svelte Extension!";
</script> -->
  

	
 <!-- main {
	text-align: center;
	padding: 20px;
}

h1 {
	color: #3498db;
}

p {
	color: #555;
}  -->




<!-- <main>
<h1>{message}</h1>
<p>This is a simple Svelte component for your Chrome extension popup.</p>
</main> -->
  