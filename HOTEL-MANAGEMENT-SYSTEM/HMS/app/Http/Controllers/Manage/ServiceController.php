<?php

namespace App\Http\Controllers\Manage;

use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use App\User;
use App\Guest;
use App\Booking;
use App\Room;
class ServiceController extends Controller
{
    public function __construct(){
        $this->middleware('auth');
    }
   
    public function bookingRoomGet($name){
        $data['title'] = "Make reservation";
        $data['nameroom'] = $name;
        $data['receiption'] = User::where('role', '0')->get(); //0: receiption  1: director
            return view('receiption/bookingroom',$data);
    }
    public function bookingRoomPost(Request $request){
        $data['title'] = "Make reservation";
        //save to guest table
        $guest = new Guest;
        $guest = $request->all();
        $guest_id = Guest::create($guest);
       
        //save to booking table
        $booking = new Booking;
        $booking = $request->all();     
        $booking['guest_id'] = $guest_id->id;
        Booking::create($booking);

        //update status room
        Room::where('name', $booking['room_name'])->update(array('status'=> 'N'));
        
             return redirect()->route('listbooking_com');
    }
    public function listBooking(){
         $data['title'] = "LIST BOOKING";
         $data['booking'] = Booking::all();
         return view('default/listBooking',$data);
    }
    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //add new service
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
