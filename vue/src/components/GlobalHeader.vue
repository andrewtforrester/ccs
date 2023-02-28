<template>
	<header :class="{ 'text-white': lighttop=='Yes', 'text-white': lighttop=='No' }" class="absolute z-[1000] top-0 left-0 right-0 px-6 sm:px-10 py-6">
		<div class="flex items-center justify-between">
			<a class="relative" href="/">
				<div class="flex items-center">
					<div :class="{ 'bg-navy': this.lighttop=='Yes', 'bg-white': this.lighttop=='No' }" class="h-[2rem] w-[2rem] rounded-full mr-4">
					</div>
					<div :class="{ 'text-white': lighttop=='Yes', 'text-white': lighttop=='No' }" class="hidden font-serif text-xl italic font-bold leading-6 lg:block">
						Center for Christianity <br> and Scholarship
					</div>
				</div>
			</a>
			
			<menu>
				<div class="flex items-center justify-bewtween">
					<div class="relative hidden ml-4 sm:block group">
						<h1 class="text-lg font-bold hover:cursor-pointer">About</h1>
	
						<div class="absolute top-10 overflow-y-hidden whitespace-nowrap h-0 rounded-[.2rem] transition-all bg-navy px-4 ease-in-out duration-300 transform group-hover:h-auto group-hover:py-4 text-white">
							<a href="/about">
								<h2 class="text-md hover:text-rose">Who We Are</h2>
							</a>
							<a href="/house">
								<h2 class="text-md hover:text-rose">House</h2>
							</a>
							<a href="/leadership">
								<h2 class="text-md text hover:text-rose">Leadership</h2>
							</a>
							<a href="/faculty-affiliates">
								<h2 class="text-md hover:text-rose">Faculty Affiliates</h2>
							</a>
						</div>
					</div>

					<div class="relative hidden ml-4 sm:block group">
						<h1 class="text-lg font-bold hover:cursor-pointer">Events</h1>

						<div class="absolute top-10 overflow-y-hidden whitespace-nowrap h-0 rounded-[.2rem] transition-all bg-navy px-4 ease-in-out duration-300 transform group-hover:h-auto group-hover:py-4 text-white">
							<a href="/calendar">
								<h2 class="text-md hover:text-rose">Calendar</h2>
							</a>
							<a href="/courses">
								<h2 class="text-md hover:text-rose">Courses</h2>
							</a>
							<a href="/reading-groups">
								<h2 class="text-md hover:text-rose">Reading Groups</h2>
							</a>
							<a href="/wwm">
								<h2 class="text-md hover:text-rose">Weekly Wednesday Meal</h2>
							</a>
							<a href="/lectures">
								<h2 class="text-md hover:text-rose">Lectures</h2>
							</a>
							<a href="/conferences">
								<h2 class="text-md hover:text-rose">Conferences</h2>
							</a>
						</div>
					</div>

					<!-- <div class="relative hidden ml-4 sm:block group">
						<h1 class="text-lg font-bold hover:cursor-pointer">Undergrads</h1>
	
						<div class="absolute top-10 overflow-y-hidden whitespace-nowrap h-0 rounded-[.2rem] transition-all bg-navy px-4 ease-in-out duration-300 transform group-hover:h-auto group-hover:py-4 text-white">
							<a href="/construction">
								<h2 class="text-md hover:text-rose">Incoming Students</h2>
							</a>
							<a href="/certification-pathway">
								<h2 class="text-md hover:text-rose">Certification Pathway</h2>
							</a>
							<a href="/fellows-program">
								<h2 class="text-md hover:text-rose">Fellows Program</h2>
							</a>
						</div>
					</div> -->

					<!-- <div class="relative hidden ml-4 sm:block group">
						<h1 class="text-lg font-bold hover:cursor-pointer whitespace-nowrap">Grad Students</h1>
	
						<div class="absolute top-10 overflow-y-hidden whitespace-nowrap h-0 rounded-[.2rem] transition-all bg-navy px-4 ease-in-out duration-300 transform group-hover:h-auto group-hover:py-4 text-white">
							<a href="/graduate-christian-scholars">
								<h2 class="text-md hover:text-rose">Christian Scholars</h2>
							</a>
							<a href="/christian-scholarship-workshop">
								<h2 class="text-md hover:text-rose">Scholarship Workshop</h2>
							</a>
						</div>
					</div> -->
					
					
					<!-- <div class="relative hidden ml-4 sm:block group">
						<h1 class="text-lg font-bold hover:cursor-pointer">Faculty</h1>

						<div class="absolute top-10 overflow-y-hidden whitespace-nowrap h-0 rounded-[.2rem] transition-all bg-navy px-4 ease-in-out duration-300 transform group-hover:h-auto group-hover:py-4 text-white">
							<a href="/triangle-roundtable">
								<h2 class="text-md hover:text-rose">Triangle Roundtable</h2>
							</a>
							<a href="/faculty-reading-groups">
								<h2 class="text-md hover:text-rose">Faculty Reading Groups</h2>
							</a>
							<a href="/scholarship-workshop">
								<h2 class="text-md hover:text-rose">Scholarship Workshop</h2>
							</a>
						</div>
					</div> -->

					<div class="relative hidden ml-4 sm:block group">
						<h1 class="text-lg font-bold hover:cursor-pointer">Support</h1>

						<div class="absolute top-10 overflow-y-hidden whitespace-nowrap h-0 rounded-[.2rem] transition-all bg-navy px-4 ease-in-out duration-300 transform group-hover:h-auto group-hover:py-4 text-white">
							<!-- <a href="/continuing-education">
								<h2 class="text-md hover:text-rose">Continuing Eduation</h2>
							</a>--> 
							<a href="/lend-a-hand">
								<h2 class="text-md hover:text-rose">Lend a Hand</h2>
							</a>
							<a href="/give">
								<h2 class="text-md hover:text-rose">Donate</h2>
							</a>
						</div>
					</div>

					

					<div class="hidden ml-4 md:block">
						<button>
							<a href="/give">
								<div class="px-4 py-1 text-lg font-bold transition duration-200 ease-in-out transform border-2 rounded-full"
								:class="{ 'border-blue text-navy hover:bg-navy hover:border-navy hover:text-white': lighttop=='Yes', 'border-white text-white hover:bg-white hover:text-navy': lighttop=='No' }">
									Give
								</div>
							</a>
						</button>
					</div>
					<div class="flex ml-8 sm:hidden">
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
		props: ['lighttop'],
		data() {
			return {

			}
		}
	}
</script>
