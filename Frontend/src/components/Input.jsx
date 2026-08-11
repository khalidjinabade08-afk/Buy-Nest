import React from 'react'

const Input = (props) => {
  return (
    <>
    
            <div className="mt-1 p-2">
              <div className="relative w-80">
                <input         
                  type={props.type}
                  id={props.name}
                  name={props.name}
                  value={props.value || ""}
                  onChange={props.onChange}
                  placeholder=" "
                  className="peer w-80 h-13 rounded-lg border border-[#d9dedd] bg-white px-4 py-3 text-[#333333] outline-none transition-all focus:border-[#0f817a]! focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)] "
                />

                <label
                  htmlFor={props.name}
                  className="absolute left-4 top-1/2 -translate-y-1/2 bg-white px-1 text-[#777777] transition-all
                  peer-focus:top-0
                  peer-focus:text-sm
                  peer-focus:text-[#0f817a]
                  peer-not-placeholder-shown:top-0
                  peer-not-placeholder-shown:text-sm"
                >
                  {props.placeholder}
                </label>
              </div>
            </div>
    </>
  )
}

export default Input
