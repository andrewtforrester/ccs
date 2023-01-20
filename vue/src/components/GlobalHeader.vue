<template>
	<header class="absolute z-[1000] top-0 left-0 right-0 px-6 sm:px-10 py-6">
		<div class="flex items-center justify-between">
			<a class="relative" href="/">
				<div class="flex items-center">
					<div class="bg-white h-[2rem] w-[2rem] rounded-full mr-4">
					</div>
					<div class=" text-xl font-bold font-serif text-white leading-6 italic hidden lg:block">
						Center for Christianity <br> and Scholarship
					</div>
				</div>
			</a>
			
	
			<menu>
				<div class="flex items-center justify-bewtween">
					<div class="ml-4 relative hidden sm:block group">
						<h1 class="text-lg font-bold hover:cursor-pointer">About</h1>
	
						<div class="absolute overflow-y-hidden whitespace-nowrap h-0 rounded-[.2rem] transition-all bg-navy px-4 ease-in-out duration-300 transform group-hover:h-auto group-hover:py-4 text-white">
							<a href="">
								<h2 class="text-md hover:text-rose">Who We Are</h2>
							</a>
							<a href="">
								<h2 class="text-md hover:text-rose">Our Staff</h2>
							</a>
							<a href="">
								<h2 class="text-md hover:text-rose">Our Faculty</h2>
							</a>
						</div>
					</div>

					<div class="ml-4 relative hidden sm:block group">
						<h1 class="text-lg font-bold hover:cursor-pointer">Students</h1>
	
						<div class="absolute overflow-y-hidden whitespace-nowrap h-0 rounded-[.2rem] transition-all bg-navy px-4 ease-in-out duration-300 transform group-hover:h-auto group-hover:py-4 text-white">
							<a href="">
								<h2 class="text-md hover:text-rose">Incoming Students</h2>
							</a>
							<a href="">
								<h2 class="text-md hover:text-rose">Certification Pathway</h2>
							</a>
							<a href="">
								<h2 class="text-md hover:text-rose">Fellows Program</h2>
							</a>
							<a href="">
								<h2 class="text-md hover:text-rose">Courses</h2>
							</a>
							<a href="">
								<h2 class="text-md hover:text-rose">Mentorship</h2>
							</a>
							<a href="">
								<h2 class="text-md hover:text-rose">Grad Students</h2>
							</a>
						</div>
					</div>
					
					
					<div class="hidden sm:block">
						<div class="ml-4 relative peer">
							<h1 class="text-lg font-bold">Faculty</h1>
						</div>
					</div>
					
					<div class="hidden sm:block">
						<div class="ml-4 relative peer">
							<h1 class="text-lg font-bold">Friends</h1>
						</div>
					</div>
					
					<div class="hidden sm:block">
						<a href="">
							<div class="ml-4 relative peer">
								<h1 class="text-lg font-bold">House</h1>
							</div>
						</a>
					</div>
					
					<div class="ml-4 hidden sm:block">
						<button>
							<a href="/events">
								<div class="font-bold text-lg bg-navy px-4 py-1 rounded-full border-2 border-navy text-gray transition ease-in-out duration-200 transform hover:bg-transparent hover:text-navy">
									Events
								</div>
							</a>
						</button>
					</div>
					<div class="ml-4 hidden md:block">
						<button>
							<a href="/give">
								<div class="font-bold text-lg bg-navy px-4 py-1 rounded-full border-2 border-navy text-gray transition ease-in-out duration-200 transform hover:bg-transparent hover:text-navy">
									Give
								</div>
							</a>
						</button>
					</div>
					<div class="ml-8 flex sm:hidden">
						<div class="mr-[.15rem] bg-black h-[.3rem] w-[.3rem] rounded-full">
						</div>
						<div class="mr-[.15rem] bg-black h-[.3rem] w-[.3rem] rounded-full">
						</div>
						<div class="mr-[.15rem] bg-black h-[.3rem] w-[.3rem] rounded-full">
						</div>
					</div>
				</div>
			</menu>
		</div>
	</header>
</template>

<script>
	export default {
		name: 'GlobalHeader',
		props: {

		},
		data() {
			return {

			}
		}
	}
</script>
