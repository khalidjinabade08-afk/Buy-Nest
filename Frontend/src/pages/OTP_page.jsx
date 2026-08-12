import React from 'react'

const OTP_page = (props) => {
  return (
    <>

        <div className="min-h-screen flex items-center justify-center bg-[#F8F7F4] p-4">

            <div className="w-full max-w-80 h-110 rounded-3xl shadow-lg overflow-hidden bg-[#FFFFFF] flex">

                <div className='mt-1 p-2'>
                    <div className='relative w-3'>
                        <input 
                            type='number'
                            // id='number'
                            name='OTP'
                            // value={props.value || ""}
                            // onChange={props.onChange}
                            className="peer w-80 h-13 rounded-lg border border-[#d9dedd] bg-white px-4 py-3 text-[#333333] outline-none transition-all focus:border-[#0f817a]! focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)] "
                         />
                    </div>

                </div>
            </div>
        /</div>
      
    </>
  )
}

export default OTP_page
