<template>
	<div>
		<div class="mb-6">
			<h2 class="title-3 pb-2">{{ name }}</h2>
			<div class="title-4 pb-6">{{ title }}</div>
	
			<div v-on:click="isOpen = !isOpen" class="title-4 hover:cursor-pointer">Read more →</div>
		</div>

		<div :class="{ 'z-[-50] opacity-0': !isOpen, 'z-[110] opacity-1': isOpen }" class="text-left fixed inset-0 flex items-center justify-center transition-opacity duration-300 ease-in-out transform">
			<div class="bg-white h-full sm:h-auto border-rose border-4 p-10">
				<div class="h-full flex items-center sm:block">
					<div>
						<div class="flex items-center justify-between mb-6">
							<div class="flex items-center">
								<div class="w-[8rem] h-[8rem] rounded-full overflow-hidden mr-6">
									<img class="w-[8rem] h-[8rem]" :src="photo" alt="">
								</div>
								<div>
									<h2 class="title-3 text-navy">{{ name }}</h2>
									<div class="title-4 text-navy">{{ title }}</div>
								</div>
								
							</div>
							<div v-on:click="isOpen = !isOpen" class="hidden sm:block font-bold text-3xl text-navy hover:cursor-pointer">
								✕
							</div>
		
						</div>
						
						
						<div class="body-text-1 text-navy max-w-[40rem]">{{ description }}</div>
		
						<div v-on:click="isOpen = !isOpen" class="sm:hidden font-bold text-4xl text-navy hover:cursor-pointer text-center mt-10">
							✕
						</div>
					</div>
				</div>
				
				
			</div>
			
		</div>
		
		<div :class="{ 'opacity-0 z-[-50]': !isOpen, 'opacity-[0.9] z-[100]': isOpen }" class="fixed inset-0 bg-navy transition-opacity duration-500 ease-in-out transform">

		</div>
	</div>
</template>

<script>
	export default {
		name: 'LeaderModals',
		props: ['name','title','description','photo'],
		data() {
			return {
				isOpen: false,
			}
		}
	}
</script>
