<template>
    <div class="container mx-auto py-6 px-4 font-mono">
      <div class="mt-5 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        <button v-for="candidate in candidates" :key="candidate.user_id" @click="voteCandidate(candidate.user_id)" :class="['bg-white outline p-4 text-center', { 'animate__animated animate__tada': candidate.user_id === clickedCandidate }]">
          <img :src="candidate.avatar" alt="candidate avatar" class="w-24 h-24 outline mx-auto mb-4"/>
          <p class="font-bold text-lg">{{ candidate.username }}</p>
          <span class="text-gray-600">votos: <span class="text-black font-bold">{{ candidate.votes }}</span></span>
        </button>
      </div>
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        candidates: [],
        socket: null,
        clickedCandidate: null,
      };
    },
    mounted() {
      this.initializeWebSocket();
    },
    methods: {
      initializeWebSocket() {
        this.socket = new WebSocket('/ws/candidate/');
        this.socket.onopen = () => {
          console.log('WebSocket connected!');
        };
        this.socket.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data);
            this.updateCandidates(data);
          } catch (error) {
            console.error('Error parsing message:', error);
          }
        };
        this.socket.onclose = () => {
          console.log('WebSocket disconnected.');
        };
        this.socket.onerror = (error) => {
          console.error('WebSocket error:', error);
        };
      },
      voteCandidate(user_id) {
        this.clickedCandidate = user_id;
        axios
          .patch(`/api/candidates/${user_id}/vote/`)
          .then((response) => {
            console.log(response);
            setTimeout(() => {
              this.clickedCandidate = null;
            }, 1000);
          })
          .catch((error) => {
            console.error('Error voting for candidate:', error);
          });
      },
      updateCandidates(data) {
        this.candidates = data;
      },
    },
    beforeDestroy() {
      if (this.socket) {
        this.socket.close();
      }
    },
  };
</script>
  