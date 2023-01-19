<template>
	<header class="p-6 sm:p-10 absolute left-0 right-0 top-0 z-[100]">
		<div class="flex items-center justify-between">
			<a href="/">
				<div class="flex items-center">
					<div class="bg-navy h-[2rem] w-[2rem] rounded-full mr-4">
					</div>
					<div class="text-xl text-navy font-bold font-serif text-navy leading-6 italic">
						Center for Christianity <br> and Scholarship
					</div>
				</div>
			</a>
			
	
			<menu>
				<div class="flex items-center justify-bewtween">
					<div class="ml-4 relative">
						<h1 class="text-lg font-bold peer">About</h1>
	
						<div class="absolute whitespace-nowrap hidden peer-hover:block">
							<h2 class="text-sm">What We Do</h2>
							<h2 class="text-sm">Our Staff</h2>
							<h2 class="text-sm">Our Faculty</h2>
						</div>
					</div>
					
					<div class="ml-4 relative">
						<h1 class="text-lg font-bold peer">Students</h1>
	
						<div class="absolute whitespace-nowrap hidden peer-hover:block">
							<h2 class="text-sm">Incoming Students</h2>
							<h2 class="text-sm">Certification Pathway</h2>
							<h2 class="text-sm">Fellows Program</h2>
							<h2 class="text-sm">Short Courses</h2>
							<h2 class="text-sm">Mentorship Opportunities</h2>
							<h2 class="text-sm">Grad Students</h2>
						</div>
					</div>
					<div class="ml-4 relative peer">
						<h1 class="text-lg font-bold">Faculty</h1>
					</div>
					<div class="ml-4 relative peer">
						<h1 class="text-lg font-bold">Friends</h1>
					</div>
					<a href="">
						<div class="ml-4 relative peer">
							<h1 class="text-lg font-bold">House</h1>
						</div>
					</a>
					<div class="ml-4">
						<button>
							<a href="">
								<div class="font-bold text-lg bg-navy px-4 py-1 rounded-full border-2 border-navy text-gray transition ease-in-out duration-200 transform hover:bg-transparent hover:text-navy">
									Events
								</div>
							</a>
						</button>
					</div>
					<div class="ml-4">
						<button>
							<a href="">
								<div class="font-bold text-lg bg-navy px-4 py-1 rounded-full border-2 border-navy text-gray transition ease-in-out duration-200 transform hover:bg-transparent hover:text-navy">
									Donate
								</div>
							</a>
						</button>
					</div>
					<div class="ml-8 flex lg:hidden">
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
