<template>
	<div class="flex justify-between">
		<div class="relative">
			<div class="relative z-20 flex flex-wrap justify-between max-w-[22rem]">
				<input class="border-b-2 border-white bg-transparent text-white rounded-md w-[48%] mb-2" type="text" placeholder="First Name">
				<input class="border-b-2 border-white bg-transparent text-white rounded-md  w-[48%] mb-2" type="text" placeholder="Last Name">
				<input class="block border-b-2 border-white bg-transparent text-white rounded-md  w-full w-[100%] mb-2" type="text" placeholder="Email Address">
				<button v-on:click="sf" class="relative block">
					<div class="px-4 py-1 text-lg text-white transition duration-200 ease-in-out transform border-2 border-white rounded-full hover:bg-white hover:text-navy">
						Submit
					</div>  
				</button>
			</div>
			

			<div :class="{ 'invisible': !form_cover_active, 'visible bg-white z-[50]': form_cover_active }" class="absolute inset-0 flex items-center justify-center duration-300 transform transition-color ease-in-our">
				<div class="h-[2rem] w-[2rem] bg-burgundy rounded-full animate-ping">
				</div>
			</div>	

			<div :class="{ 'invisible': !form_cover_active2, 'visible bg-white z-[60]': form_cover_active2 }" class="absolute inset-0 flex items-center justify-center duration-300 transform transition-color ease-in-our">
				<h2 class="font-serif text-3xl italic font-bold">Thank you! </h2>
			</div>
		</div>
	</div>
		
</template>

<script>
	export default {
		name: 'GlobalMenu',
		props: {
			
		},
		data () {
			return {
				form_cover_active: false,
				form_cover_active2: false,
			}
		},
		methods: {
			sf() {	
				this.form_cover_active = true;

				setTimeout(() => this.form_cover_active2 = true, 2500);

			}
		}
	}
</script>
