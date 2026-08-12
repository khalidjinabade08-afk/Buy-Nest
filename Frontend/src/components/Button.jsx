import React from 'react'

const Button = (props) => {
  return (
    <>
    <div className="mt-1 p-2">
        <button
            type={props.type || "button"}
            onClick={props.onClick}
            className="w-80! cursor-pointer rounded-3xl! border border-[#0f817a] bg-[#0f817a] px-6 py-3 font-medium text-white hover:bg-[#0c6f69]"
        >
            {props.name}
        </button>
    </div>
    </>
  )
}

export default Button
