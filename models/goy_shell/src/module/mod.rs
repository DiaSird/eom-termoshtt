//! Example nonlinear ODEs

pub mod goy_shell_model;
pub mod semi_implicit;
pub mod traits;
pub mod adaptor;

pub use crate::module::goy_shell_model::GoyShell;
pub use crate::module::semi_implicit::DiagRK4;
pub use crate::module::traits::*;
pub use crate::module::adaptor::*;



