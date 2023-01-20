<template>
	<div class="flex">
		<div class="relative">
			<div class="relative z-20 ">
				<input class="border-b-2 border-white bg-transparent text-white rounded-md  mr-1 w-[12rem] mb-2" type="text" placeholder="First Name">
				<input class="border-b-2 border-white bg-transparent text-white rounded-md  ml-1 w-[12rem]" type="text" placeholder="Last Name">
				<input class="block border-b-2 border-white bg-transparent text-white rounded-md  w-full w-[24.5rem] mb-2" type="text" placeholder="Email Address">
				<button v-on:click="sf" class="relative block">
					<div class="px-4 py-1 border-2 border-white text-white text-lg rounded-full transition ease-in-out duration-200 transform hover:bg-white hover:text-navy">
						Submit
					</div>  
				</button>
			</div>
			

			<div :class="{ 'invisible': !form_cover_active, 'visible bg-white z-[50]': form_cover_active }" class="absolute inset-0 transition-color ease-in-our duration-300 transform flex items-center justify-center">
				<div class="h-[2rem] w-[2rem] bg-burgundy rounded-full animate-ping">
				</div>
			</div>	

			<div :class="{ 'invisible': !form_cover_active2, 'visible bg-white z-[60]': form_cover_active2 }" class="absolute inset-0 transition-color ease-in-our duration-300 transform flex items-center justify-center">
				<h2 class="text-3xl font-bold italic font-serif">Thank you! </h2>
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
