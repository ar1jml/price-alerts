import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'

import Login from '../../src/views/Login.vue'

describe('Login.vue', () => {
  it('renders the login page', () => {
    const wrapper = mount(Login)

    expect(wrapper.exists()).toBe(true)
  })
})