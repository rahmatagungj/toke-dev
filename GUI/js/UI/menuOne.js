export default function menuOne(){
	var menuOne = new Vue({
		el: '#menu-one',
		data: {
			color1: '#409EFF',
			show: true,
			text_main: 'Tips and Tricks',
			content1: [
				{title : ' Text Editor', text: 'Use the built-in text editor to speed up the editing process.'},
				{title : ' Tools', text: 'Visit the tools tab to get the full action on the app.'},
			],
			content2: [
				{title : ' Email sender', text: 'Privacy and data can be stored online via email easily.'},
				{title : ' Compatibility', text: 'OS compatible version to get the best experience.'},
			],
			card1:{
				color: 'black',
				border: '0px !important',
				backgroundColor: 'transparent'
			},
			card2: {
				color: 'white',
				border: '0px !important',
				backgroundColor: 'rgba(255, 255, 255, .15)',
				backdropFilter: 'blur(5px)'
			}
		},
		components: {
			'jumbotron': {
				template: `<div class="jumbotron">
							<h1 class="display-4">Hello!</h1>
							<p class="lead">Thank you for using the toke system, enjoy.</p>
							<hr class="my-4">
							<a class="btn btn-info" href="https://github.com/rahmatagungj/toke/discussions/new" role="button" target="_blank"><i class="fas fa-bug"></i> Report bug</a>
						</div>`
			}
		}
	})
}