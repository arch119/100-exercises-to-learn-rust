// TODO: Define a new `SaturatingU16` type.
//   It should hold a `u16` value.
//   It should provide conversions from `u16`, `u8`, `&u16` and `&u8`.
//   It should support addition with a right-hand side of type
//   SaturatingU16, u16, &u16, and &SaturatingU16. Addition should saturate at the
//   maximum value for `u16`.
//   It should be possible to compare it with another `SaturatingU16` or a `u16`.
//   It should be possible to print its debug representation.
//
// Tests are located in the `tests` folder—pay attention to the visibility of your types and methods.
//
//
use std::ops::Add;

#[derive(PartialEq, Debug, Copy)]
pub struct SaturatingU16{
    val: u16,
}


impl Clone for SaturatingU16{
    fn clone(&self) -> Self{
        SaturatingU16{
            val: self.val
        }
    }
}

impl PartialEq<u16> for SaturatingU16{
    fn eq(&self, other: &u16) -> bool{
        self.val == *other
    }
}

impl Add for SaturatingU16{
    type Output = Self ;

    fn add(self, val: Self) -> Self::Output {
        SaturatingU16{
            val: self.val.saturating_add(val.val)
        }
    }
}

impl Add<u16> for SaturatingU16{
    type Output = Self ;

    fn add(self, val: u16) -> Self::Output {
        SaturatingU16{
            val: self.val.saturating_add(val)
        }
    }
}

impl Add<&u16> for SaturatingU16{
    type Output = Self ;

    fn add(self, val: &u16) -> Self::Output {
        SaturatingU16{
            val: self.val.saturating_add(*val)
        }
    }
}

impl Add<&SaturatingU16> for SaturatingU16{
    type Output = Self ;

    fn add(self, val: &SaturatingU16) -> Self::Output {
        SaturatingU16{
            val: self.val.saturating_add(val.val)
        }
    }
}

impl From<u16> for SaturatingU16{
    fn from(val: u16) -> Self{
        SaturatingU16{
            val
        }
    }
}


impl From<u8> for SaturatingU16{
    fn from(val: u8) -> Self{
        SaturatingU16{
            val: val.into()
        }
    }
}

impl From<&u16> for SaturatingU16{
    fn from(val: &u16) -> Self{
        SaturatingU16{
            val: *val
        }
    }
}

impl From<&u8> for SaturatingU16{
    fn from(val: &u8) -> Self{
        SaturatingU16{
            val: (*val).into()
        }
    }
}


