<template>
    <div>
      <div class="tab-buttons">
        <button v-for="(tab, index) in tabs" :key="index" @click="changeTab(index)" :class="{ 'active': activeTab === index }">{{ tab.label }}</button>
      </div>
      <div class="tab-content">
        <slot></slot>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        activeTab: 0,
        tabs: [],
      };
    },
    methods: {
      changeTab(index) {
        this.activeTab = index;
      },
    },
    created() {
      this.tabs = this.$children.map((child) => ({
        label: child.$attrs.tab,
      }));
    },
  };
  </script>
  
  <style scoped>
  .tab-buttons {
    display: flex;
  }
  
  .tab-buttons button {
    cursor: pointer;
    padding: 10px;
    margin-right: 5px;
    border: none;
    background-color: #f0f0f0;
  }
  
  .tab-buttons button.active {
    background-color: #ddd;
  }
  
  .tab-content {
    margin-top: 10px;
  }
  </style>